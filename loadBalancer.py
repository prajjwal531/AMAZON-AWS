#This file is used to  create load balancer
import  boto3
import sys
ec2 = boto3.client('elb')

response = ec2.describe_load_balancers(
    LoadBalancerNames=[
        'Apache',
    ],

)


print response
ec3=boto3.client('ec2')
response = ec3.describe_availability_zones(
)
print response


r=ec3.describe_security_groups(
                    GroupNames=[
                        'ec2-sg'
                    ]
                )
t=r.get('SecurityGroups')[0]
print t.get('GroupId')
for a in t:
    print a
print r.get('UserIdGroupPairs')

ec2 = boto3.resource("ec2")

print ec2.vpcs.all()
for vpc in ec2.vpcs.all():
    for subnet in vpc.subnets.all():
        print vpc,subnet
#sys.exit(1)

ec2 = boto3.client('elb')
response = ec2.create_load_balancer(
    LoadBalancerName='apache3',
    Listeners=[
        {
            'Protocol': 'http',
            'LoadBalancerPort': 80,
            'InstanceProtocol': 'http',
            'InstancePort': 80
        },
    ],
    AvailabilityZones=[
        'us-west-2c',
    ],
    SecurityGroups=[
        'sg-90ba55ed',
    ],
    Tags=[
        {
            'Key': 'name',
            'Value': 'hello'
        },
    ]
)

