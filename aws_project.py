import boto3
import yaml

f = open('data.yml')
class aws:

       def __init__(self):
           self.ec2 = boto3.client('ec2')
           self.ec2_resource = boto3.resource('ec2')
           self.yml = yaml.load(f)
           response = self.ec2.describe_vpcs()
           d = response.get('Vpcs')
           self.VpcId = d[0].get('VpcId')
           print self.yml.get('SecurityGroups')