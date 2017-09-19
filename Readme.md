# Project Title

This Project is to setup AWS instance and Implement a webapplication

## Getting Started

These instructions will allow you to spin up new instances in AWS console and will help you to deploy code to tomcat.

### Prerequisites

In-order for this application to work, we need boto3 and ansible installed on client machine.
you can install them by using following commands.

```
pip install boto3
sudo (yum|apt) depending on linux ansible
on mac it can be using brew
```
### Seting up environment
This is the first step and required in order to get started. we need to run environmentsetup.sh and pass three arguments in given order below.
1. aws_access_key_id
2. aws_secret_access_key
3. region

#### Example:  bash environmentsetup.sh 'aws_access_key_id' 'aws_secret_access_key' 'region'

This script will set up a default profile for boto to use.

#### Note: This Script creates a default profile. creating a custom profile can be added as an extension.

## Creating Instance on AWS
aws.py is the script that creates all resources to AWS. aws.py reads the configurations from data.yml and creates following resources.

1. SecurityGroups: This enables incoming and outgoing traffic to and from resources.
2. EC2 Instance: These are the environments being created.
3. Load Balancer: It serves as parent for all EC2 instances and distribute the traffic based on load.
4. RDS DB (MySQL): This database is created to store transaction made by sample webapp.

## 3. Specifications of data.yml

1. **EC2-Instance > InstanceX** : This has all required parameters needed to create EC2-Instance. we can define as many instance we want to create.
if we do not want to create same instance further, set up "re-create: False" in data.yml in that Instance section.
2. **SecurityGroups:** This section is used to define security groups and their inBound_mapping and outBound_mapping.
3. **LoadBalancer:** This section is used to create load balancer and also tells us the details of instances needs to be registered with it.
4. **RDS:** This section is used to define RDS information. (RDS was created manually)


## Run Aws.py
  We need to make sure that data.yml and aws.py are in same folder when aws.py is executed. Once run it will create new ec2 instances, attach security groups to it and creates a load balancer.

  ## Working flow

  Load Balancer is consumer facing and redirects incoming traffic. It takes traffic on both secure and non secure port and transmit it to non secure port to ec2
  instances. Same was achieved by defining this topology in listeners.

    LB        EC2
    8080 ===> 8080

    443 ====> 8080

  Each instance is deployed into different AvailabilityZone, this information is defined in data.yml.
  This could have been avoided using Autoscaling where it creates the instances in same region but it tries to create them in seperate zones. (This could have been an enhancement to this application)

  A custom build image is used in this solution and it has java and tomcat installed. Same ami-id is being used to create multiple instances.
  After sucessfull resource creation in AWS, we can start deploying code to both tomcat instances.

  we will use ansible dynamic inventory to do deployments to ec2 instances. we have identified these EC2-Instance as webserver and used specific keyname to configure them. Hence while running ansible we will use "key_'keyname'" to identify all webserver for deployment.
  Once the war file is deployed and tomcat restarted it can be accessed via both http and https port using LoadBalancer DNS.

  ### Note:
           Since this solution reads the data from data.yml, any information such as keyname, ami-id, SSLCertificateId should be replaced based on the instance is being used.

## Deployment info

To start the deployment we have already built the war file and setup db information in the code to access rds db.
after checking sucessfully testing dynamic inventory setup, we can run this playbook using command give below.
The link to setup dynamic inventory in your local machine can be found [here](https://aws.amazon.com/blogs/apn/getting-started-with-ansible-and-dynamic-amazon-ec2-inventory-management/).
Also, most of this setup are being taken care by "environmentsetup.sh" script that we have run initially.

 #### ansible-playbook deployment.yml

After running this playbook it will deploy this war file to tomcat and restart it.
It is a Java based webservice deployed on tomcat instances and it can be access over this Id.

"https://apache2-2071546822.us-west-2.elb.amazonaws.com/transactions/webapi/accounts/243406451234"

where it is getting the data from rds db based on account id.
