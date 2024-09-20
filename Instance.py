import boto3
import sys

region = sys.argv[1]
access_key = sys.argv[2]
secret_key = sys.argv[3]

client = boto3.client('ec2' region_name=region,aws_access_key_id=access_key,aws_secret_access_key=secret_key)
response = client.describe_instances(
    Filters=[
        {
            'Name': 'Instance-type',
            'Values': [
                't2.small',
            ],
        },
    ],
)

print(response)
