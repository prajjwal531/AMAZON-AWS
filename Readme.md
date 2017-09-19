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
3. **LoadBalancer:** This section is used to create load balance and it registers the instances. Also this section specifies the Listeners
that this LoadBalancer will use to listen and redirect. Instance-name should be listed in this section in-order to register it with load balancer. if listenr is listening to https port, we need to specify SSLCertificateId as well in data.yml.
4. **RDS:** This section is used to define RDS information. (RDS was created manually)
