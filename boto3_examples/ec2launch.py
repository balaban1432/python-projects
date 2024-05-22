import boto3

client = boto3.client('ec2')

# create a new EC2 instance
response = client.run_instances(
    ImageId='ami-04b70fa74e45c3917',
    InstanceType='t2.micro',
    KeyName='derya',
    MaxCount=1,
    MinCount=1,
)

print(response)