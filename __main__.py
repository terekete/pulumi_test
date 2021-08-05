import yaml
import pulumi
from pulumi_gcp import storage, bigquery

# # Create a GCP resource (Storage Bucket)
# bucket = storage.Bucket('my-bucket')
# # dataset = bigquery.Dataset(resource_name='my-dataset', dataset_id='my_dataset')

# # Export the DNS name of the bucket
# pulumi.export('bucket_name', bucket.url)

print(dir(pulumi))


def update(path):
    with open(path + 'manifest.yaml') as f:
        manifest = yaml.safe_load(f)
        print(manifest)
        dataset = bigquery.Dataset(resource_name=manifest['resource_name'], dataset_id=manifest['dataset_id'])


f = open('/workspace/DIFF_DATASETS.txt')
path_list = f.read().splitlines()
print(path_list)


# result = [do_something(x) for x in list if list]
for path in path_list:
    update(path)

