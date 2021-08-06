import yaml
import pulumi
from pulumi_gcp import storage, bigquery


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
    bigquery.Table(
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
        if manifest['type'] == 'dataset':
            dataset(manifest)
        if manifest['type'] == 'table':
            table(manifest)


def update_dataset_readers(path: str) -> None:
    with open(path + 'manifest.yaml') as f:
        manifest = yaml.safe_load(f)
        if manifest['type'] == 'dataset':
            for reader in manifest['readers'] or []:
                dataset_user_access(manifest, reader, 'READER')
        else:
            print("Manifest does not exist, please add or remove empty dataset folder")


f = open('/workspace/DIFF_LIST.txt')
for path in f.read().splitlines():
    update(path)

