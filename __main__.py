import yaml
import pulumi
from pulumi_gcp import storage, bigquery

# # Create a GCP resource (Storage Bucket)
# bucket = storage.Bucket('my-bucket')
# # dataset = bigquery.Dataset(resource_name='my-dataset', dataset_id='my_dataset')

# # Export the DNS name of the bucket
# pulumi.export('bucket_name', bucket.url)

def dataset(manifest):
    return bigquery.Dataset(
        resource_name=manifest['resource_name'],
        dataset_id=manifest['dataset_id'],
        description=manifest['description'],
        labels=[{'cost_center': manifest['cost_center']}]
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


# version: v1
# type: dataset
# metadata:
#   cost_center:
#   dep:
# team: tsbt
# description: "Table for FIFA orders"
# resource_name: tsbt_fifa_orders
# dataset_id: tsbt_fifa_orders
# partition_expiration_ms: 1000
# table_expiration_ms: 1000
# friendly_name: tsbt_fifa_orders
