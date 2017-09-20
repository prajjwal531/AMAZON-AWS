import re
import json
import  yaml
import boto3
p=re.compile("([\d]+\.){3}\d*\/\d+")
print (p.match('1629.128.141/32'))

f=open('data.yml')
yml = yaml.load(f)

print yml['LoadBalancer']['Balancer1']['HealthCheck']

session = boto3.Session(profile_name='trinimbus')
# Any clients created from this session will use credentials
# from the [dev] section of ~/.aws/credentials.
dev_s3_client = session.client('ec2')
print  dev_s3_client
a=dev_s3_client.describe_security_groups()
print a
a = dev_s3_client.describe_security_groups(
    Filters=[
        {
            'Name': 'vpc-id',
            'Values': [
                "vpc-1a5da37c",
            ]
        },
    ],
    GroupNames=[
        "ec2-lb2"
    ]
)

print a