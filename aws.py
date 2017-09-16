import boto3
import yaml
import sys
from botocore.exceptions import ClientError
import re

class AWSEC2:

    def __init__(self):
        self.ec2 = boto3.client('ec2')
        self.ec2_resource = boto3.resource('ec2')
        response = self.ec2.describe_vpcs()
        d = response.get('Vpcs')
        self.VpcId = d[0].get('VpcId')
        f=open('data.yml')
        self.yml=yaml.load(f)
        print self.yml.get('SecurityGroups')


    def checkExistance(self, group):
        print "-------------Checking to see if Security Group exists------------------"
        securityGroups=group.get('SecurityGroups')
        groupInfo = []
        for securityGroup in securityGroups:
            try:
                a = self.ec2.describe_security_groups(
                    GroupNames=[
                        securityGroup
                    ]
                )
                print a
                if (a is not None):
                    print "---------------- Group with name %s exists, ----------------" % (securityGroup)
                    continue
            except ClientError as e:
                print "This Group Does not exist %s"%(securityGroup)
                GroupId = self.createSecurityGroup(securityGroup)
                print GroupId
                groupData=[securityGroup,GroupId]
                groupInfo.append(groupData)
                pass
        return groupInfo

    def createSecurityGroup(self,securityGroupName):
        print "-------This method is used to create Security Group---------------------"
        securityGroup=self.yml.get('SecurityGroups')
        for sGroups in securityGroup:
            print sGroups,securityGroupName
            if(securityGroup.get(sGroups).get('name')==securityGroupName):
                response = self.ec2.create_security_group(GroupName=securityGroupName,
                                                  Description=securityGroup.get(sGroups).get('description'),
                                                  VpcId=self.VpcId)
                security_group_id = response['GroupId']
                return security_group_id

    def getSecurityGroupId(self,groupName):
        r = self.ec2.describe_security_groups(
            GroupNames=[
                groupName
            ]
        )
        t = r.get('SecurityGroups')[0]
        return t.get('GroupId')


    def attachRules(self, groupInfo):
        for group in groupInfo:
            securityGroupName=group[0]
            securityGroupId=group[1]
            securitygroup = self.yml.get('SecurityGroups')
            for sgroups in securitygroup:
                if (securitygroup.get(sgroups).get('name') == securityGroupName):
                    mappings=securitygroup.get(sgroups).get('mappings')
                    print "this method is used to attach the rules for seurity group"
                    for mapping in mappings:
                        if (mapping == "inBound_mapping"):
                            for mapdata in mappings[mapping]:
                                print mapdata
                                p = re.compile("([\d]+\.){3}\d*\/\d+")
                                print p.match(str(mappings[mapping][mapdata].get('IpRanges')))
                                if ((p.match(str(mappings[mapping][mapdata].get('IpRanges')))) is None):
                                    range='UserIdGroupPairs'
                                    ipType ='GroupId'
                                    ipRange = self.getSecurityGroupId(mappings[mapping][mapdata].get('IpRanges'))
                                else:
                                    range = 'IpRanges'
                                    ipType = 'CidrIp'
                                    ipRange = mappings[mapping][mapdata].get('IpRanges')
                                try:
                                    print ipRange
                                    data = (self.ec2).authorize_security_group_ingress(
                                        GroupId=securityGroupId,
                                        IpPermissions=[
                                            {'IpProtocol': mappings[mapping][mapdata].get('IpProtocol'),
                                             'FromPort': mappings[mapping][mapdata].get('FromPort'),
                                             'ToPort': mappings[mapping][mapdata].get('ToPort'),
                                             range: [{ipType: ipRange}]}

                                            ])
                                    print data
                                except ClientError as e:
                                    print (e)
                                    pass
                        elif (mapping == 'outBound_mapping'):
                            print "this is a set up for outbound mapping"
                            for mapdata in mappings[mapping]:
                                t=str(mappings[mapping][mapdata].get('IpRanges'))
                                p = re.compile("([\d]+\.){3}\d*\/\d+")
                                print mappings[mapping][mapdata].get('IprRanges')
                                print (p.match(str(mappings[mapping][mapdata].get('IpRanges'))))
                                a=mappings[mapping][mapdata]
                                print a
                                if ((p.match(str(mappings[mapping][mapdata].get('IpRanges')))) is None):
                                    range = 'UserIdGroupPairs'
                                    ipType = 'GroupId'
                                    ipRange = self.getSecurityGroupId(mappings[mapping][mapdata].get('IpRanges'))
                                else:
                                    range = 'IpRanges'
                                    ipType = 'CidrIp'
                                    ipRange = mappings[mapping][mapdata].get('IpRanges')
                                try:
                                    data = (self.ec2).authorize_security_group_egress(
                                        GroupId=securityGroupId,
                                        IpPermissions=[
                                            {'IpProtocol': mappings[mapping][mapdata].get('IpProtocol'),
                                             'FromPort': mappings[mapping][mapdata].get('FromPort'),
                                             'ToPort': mappings[mapping][mapdata].get('ToPort'),
                                             range: [{ipType: ipRange}]}

                                        ])
                                    print data
                                except ClientError as e:
                                    print (e)
                                    pass


    def createInstance(self):
        print "======= This method is used to create instances======================="
        print self.ec2
        Instances = self.yml.get('EC2-Instance')
        for instance in self.yml.get('EC2-Instance'):
            if (Instances.get(instance).get('re-create')):
                group=self.checkExistance(Instances.get(instance))
                self.attachRules(group)
                print group
                try:
                    data = self.ec2_resource.create_instances(
                    BlockDeviceMappings=[
                            {
                                'DeviceName': Instances.get(instance).get('DeviceName'),
                                'VirtualName': Instances.get(instance).get('VirtualName'),
                                'Ebs': {
                                    #'Encrypted': Instances.get(instance).get('Encrypted'),#False,
                                    'SnapshotId': Instances.get(instance).get('SnapshotId'),
                                    'DeleteOnTermination': Instances.get(instance).get('DeleteOnTermination'),#True,
                                    'VolumeSize': Instances.get(instance).get('VolumeSize'),
                                    'VolumeType': Instances.get(instance).get('VolumeType')
                                },

                            },
                        ],
                        Placement={
                            'AvailabilityZone': 'us-west-2b'
                        },

                        ImageId=Instances.get(instance).get('ami-id'),
                        MinCount=Instances.get(instance).get('min-count'),
                        MaxCount=Instances.get(instance).get('max-count'),
                        InstanceType=Instances.get(instance).get('instanceType'),
                        SecurityGroups=Instances.get(instance).get('SecurityGroups'),
                        KeyName= Instances.get(instance).get('KeyName')
                    )
                    print data
                except ClientError as e:
                    print (e)
            else:
                print "--------- VM recreation is not needed at this point, checking the permission for other vm -----------"
    def getData(self):
        response = self.ec2.describe_volumes()
        print response.get('Volumes')
        for volums in response.get('Volumes'):
            print volums


if __name__ == '__main__':
    aws = AWSEC2()
    aws.createInstance()

