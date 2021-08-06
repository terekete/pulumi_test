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

def dataset_user_access(manifest, user='gates.mark@gmail.com'):
    return bigquery.DatasetAccess(
        resource_name=manifest['resource_name'],
        dataset_id=manifest['dataset_id'],
        user_by_email=user,
        role='roles/bigquery.jobUser'
    )

def update(path):
    with open(path + 'manifest.yaml') as f:
        manifest = yaml.safe_load(f)
        if manifest['type'] == 'dataset':
            dataset(manifest)
        if manifest['type'] == 'table':
            print('create table')


f = open('/workspace/DIFF_LIST.txt')
for path in f.read().splitlines():
    update(path)
