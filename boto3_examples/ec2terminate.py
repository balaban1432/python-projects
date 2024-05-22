import boto3
ec2 = boto3.resource('ec2')
ec2.Instance('i-0b28099fcbac94eb1').terminate()