import boto3

client = boto3.client('s3')

response = client.delete_bucket(
    Bucket='balaban1432',
)

print(response)