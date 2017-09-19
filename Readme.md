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

## Installing

A step by step series of examples that tell you have to get a development env running

Say what the step will be
