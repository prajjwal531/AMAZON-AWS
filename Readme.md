This Document can be used to set up local environment and know more about application process.
perquisites: Anisble and boto3 should be installed

## 1. Setup Local environment:
 This is the first step and required in order to get started. we need to run environmentsetup.sh and pass three arguments in given order below.
1. aws_access_key_id
2. aws_secret_access_key
3. region

Example:  bash environmentsetup.sh 'aws_access_key_id' 'aws_secret_access_key' 'region'

This script will set up a default profile for boto to use.

Note: This script does not support to create specific profile other then default. This feature can be added as an enhancement.

## 2. Setting up AWS instance:

 aws.py is the script that creates all resources to AWS. aws.py reads the configurations from data.yml and creates following resources.

 1. SecurityGroups: This enables incoming and outgoing traffic to and from resources.
 2. EC2 Instance: These are the environments being created.
 3. Load Balancer: It serves as parent for all EC2 instances and distribute the traffic based on load.
 4. RDS DB (MySQL): This database is created to store transaction made by sample webapp.

## 3. Specifications of data.yml

        1. EC2-Instance > InstanceX: This has all required parameters needed to create EC2-Instance. we can define as many instance we want to create.
        if we do not want to create same instance further, set up "re-create: False" in data.yml in that Instance section.

        2. SecurityGroups: This section is used to define security groups and their inBound_mapping and outBound_mapping.

        3. LoadBalancer: This section is used to create load balance and it registers the instances. Also this section specifies the Listeners
                      that this LoadBalancer will use to listen and redirect. Instance-name should be listed in this section in-order to register it with load balancer. if listenr is listening to https port, we need to specify SSLCertificateId as well in data.yml.
        4. RDS: This section is used to define RDS information. (RDS was created manually)


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

A custom build image is used in this solution that has java and tomcat installed in it and same ami-id is being used to create multiple instances.
Once the environments and LoadBalancer is up and working and tested. we can deploy the webapp to tomcat and restart it.

we will use ansible dynamic inventory to do deployments to ec2 instances. we have identified these EC2-Instance as webserver and used specific keyname to configure them. Hence while running ansible we will use "key_'keyname'" to identify all webserver for deployment.
Once the war file is deployed and tomcat restarted it can be accessed via both http and https port using LoadBalancer DNS.

## Deployment info

There is a Java based webservice deployed on tomcat instances and it can be access over this Id.

"https://apache2-2071546822.us-west-2.elb.amazonaws.com/transactions/webapi/accounts/243406451234"

where it is getting the data from rds db based on account id.
