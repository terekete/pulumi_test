"""A Google Cloud Python Pulumi program"""

import pulumi
from pulumi_gcp import storage, bigquery

# Create a GCP resource (Storage Bucket)
bucket = storage.Bucket('my-bucket')
dataset = bigquery.Dataset('my-dataset')

# Export the DNS name of the bucket
pulumi.export('bucket_name', bucket.url)
