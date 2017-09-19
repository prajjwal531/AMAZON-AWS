This Document can be used to set up local environment and know more about application process.
perquisites: Anisble and boto3 should be installed

1. Setup Local environment: This is the first step and required in order to get started. we need to run environmentsetup.sh and pass
                            three arguments in given order below.
                            1. aws_access_key_id
                            2. aws_secret_access_key
                            3. region

                          Example:  bash environmentsetup.sh 'aws_access_key_id' 'aws_secret_access_key' 'region'

                          This script will set up a default profile for boto to use.

                          Note: This script does not support to create specific profile other then default. This feature can be added as an enhancement.

2. Setting up AWS instance:  aws.py is the script that creates all resources to AWS. aws.py reads the configurations from data.yml and creates following
                             resources.

                             1. SecurityGroups: This enables incoming and outgoing traffic to and from resources.
                             2. EC2 Instance: These are the environments being created.
                             3. Load Balancer: It serves as parent for all EC2 instances and distribute the traffic based on load.


      2.1  Specifications of data.yml:

                             EC2-Instance>InstanceX: This has all required parameters needed to create EC2-Instance. we can define as many instance we want to create.
                                                     if we do not want to create same instance further, set up "re-create: False" in data.yml in that Instance section.

                            SecurityGroups: This section is used to define security groups and their inBound_mapping and outBound_mapping.

                            LoadBalancer: This section is used to create load balance and it registers the instances. Also this section specifies the Listeners
                                          that this LoadBalancer will use to listen and redirect.

                                          Instance-name should be listed in this section in-order to register it with load balancer.