
# import pulumi
# from pulumi_gcp import storage, bigquery

# # Create a GCP resource (Storage Bucket)
# bucket = storage.Bucket('my-bucket')
# # dataset = bigquery.Dataset(resource_name='my-dataset', dataset_id='my_dataset')

# # Export the DNS name of the bucket
# pulumi.export('bucket_name', bucket.url)



with open('/workspace/DIFF_DATASETS.txt', 'r') as reader:
    line = reader.readline()
    while line != '':
        print(line, end='')
        line = reader.readline()

