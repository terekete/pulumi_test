import yaml
import pulumi
from pulumi_gcp import storage, bigquery

# # Create a GCP resource (Storage Bucket)
# bucket = storage.Bucket('my-bucket')
# # dataset = bigquery.Dataset(resource_name='my-dataset', dataset_id='my_dataset')

# # Export the DNS name of the bucket
# pulumi.export('bucket_name', bucket.url)


f = open('/workspace/DIFF_DATASETS.txt')
temp = f.read().splitlines()
print(temp)

# with open('manifest.yaml') as f:
#     my_dict = yaml.safe_load(f)
#     print(my_dict)