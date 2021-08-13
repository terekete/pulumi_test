import yaml
import pulumi
from pulumi_gcp import storage, bigquery
from cerberus import Validator


def dataset(manifest: str) -> None:
    bigquery.Dataset(
        resource_name=manifest['resource_name'],
        dataset_id=manifest['dataset_id'],
        description=manifest['description'],
        labels={'cost_center': manifest['metadata']['cost_center'], 'dep': manifest['metadata']['dep']},
        default_partition_expiration_ms=manifest['partition_expiration_ms'],
        default_table_expiration_ms=manifest['table_expiration_ms'],
        delete_contents_on_destroy=True,
        location='northamerica-northeast1'
    )


def dataset_user_access(manifest: str, user: str, role: str) -> None:
    bigquery.DatasetAccess(
        resource_name=manifest['resource_name'],
        dataset_id=manifest['dataset_id'],
        user_by_email=user,
        role=role
    )


def table(manifest: str) -> None:
    return bigquery.Table(
        resource_name=manifest['resource_name'],
        dataset_id=manifest['dataset_id'],
        table_id=manifest['table_id'],
        deletion_protection=False,
        expiration_time=manifest['expiration_ms'],
        friendly_name=manifest['friendly_name'],
        labels={'cost_center': manifest['metadata']['cost_center'], 'dep': manifest['metadata']['dep']},
        schema=manifest['schema']
    )


def update(path: str) -> None:
    with open(path + 'manifest.yaml') as f:
        manifest = yaml.safe_load(f)
        if manifest and manifest['type'] == 'dataset':
            dataset(manifest)
        if manifest and manifest['type'] == 'table':
            validate_table_manifest(manifest)
            t = table(manifest)
            table_user_access(manifest, t)


# def update_access(path: str) -> None:
#         manifest = load_manifest(path)
#         if manifest and manifest['type'] == 'dataset':
#             # [dataset_user_access(manifest, reader, 'READER') for reader in manifest['readers'] if not None]
#             for reader in manifest['readers'] or []:
#                 dataset_user_access(manifest, reader, 'READER')
#             # for writer in manifest['writer'] or []:
#             #     dataset_user_access(manifest, writer, 'WRITER')
#         if manifest and manifest['type'] == 'table':
#             table_user_access(manifest)


def table_user_access(manifest, table_ref) -> None:
    readers = manifest['access']['readers']
    readers = ["user:" + reader for reader in readers]
    print(readers)
    bigquery.IamBinding(
        resource_name=manifest['resource_name'],
        dataset_id=manifest['dataset_id'],
        table_id=table_ref.table_id,
        role='roles/bigquery.dataViewer',
        members=readers
    )


def load_manifest(path):
    manifest = open(path + 'manifest.yaml', 'r')
    try:
        return yaml.safe_load(manifest)
    except yaml.YAMLError as exception:
        raise exception


def validate_table_manifest(manifest):
    schema = eval(open('./schemas/table.py', 'r').read())
    validator = Validator(schema)
    if validator.validate(manifest, schema):
        return
    else:
        print(manifest.values()[0])
        raise Exception(validator.errors)


f = open('/workspace/DIFF_LIST.txt')
for path in f.read().splitlines():
    update(path)
    # update_access(path)

