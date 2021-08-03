
# import pulumi
# from pulumi_gcp import storage, bigquery

# # Create a GCP resource (Storage Bucket)
# bucket = storage.Bucket('my-bucket')
# # dataset = bigquery.Dataset(resource_name='my-dataset', dataset_id='my_dataset')

# # Export the DNS name of the bucket
# pulumi.export('bucket_name', bucket.url)



import os

with open('DIFF_DATASETS.txt') as reader:
    print(reader.read())
