import yaml
import pulumi
from pulumi_gcp import storage, bigquery

# # Create a GCP resource (Storage Bucket)
# bucket = storage.Bucket('my-bucket')
# # dataset = bigquery.Dataset(resource_name='my-dataset', dataset_id='my_dataset')

# # Export the DNS name of the bucket
# pulumi.export('bucket_name', bucket.url)


def update(path):
    with open(path + 'manifest.yaml') as f:
        manifest = yaml.safe_load(f)
        if manifest['type'] = 'dataset':
            bigquery.Dataset(resource_name=manifest['resource_name'], dataset_id=manifest['dataset_id'])
        if manifest['type'] == 'table':
            print('create table')


f = open('/workspace/DIFF_LIST.txt')
for path in f.read().splitlines():
    update(path)

