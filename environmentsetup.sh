#!/usr/bin/env bash
# This script is used to set up local environment, please run this script as sudo



setup(){

cd ~/.aws
cat << EOF >> credentials
[default]
aws_access_key_id = $1
aws_secret_access_key = $2
EOF

cat << EOF >> config
[default]
region=$3
EOF

chmod u+rw *

}
exportData(){
          echo "--------------exporting hosts------------------"

            export ANSIBLE_HOSTS=/etc/ansible/ec2.py
            export EC2_INI_PATH=/etc/ansible/ec2.ini
            export AWS_ACCESS_KEY_ID=$1
            export AWS_SECRET_ACCESS_KEY=$2

}
setupEc2DynamicInventory(){
    echo "-----------------Setting up ec2 dynamic inventory----------------------"
    if [ -d /etc/ansible ]; then
        cd /etc/ansible
        if [ -f /etc/ansible/ec2.py ] && [ -f /ec2/ansible/ec2.ini ]; then
            echo "------------setting up inventory------------"

         else
             echo "-----------downloading the files------------"
             wget https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ec2.py
             wget https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ec2.ini
        fi
     else
         echo "Please make sure ansible is installed and this folder structure is created"
         exit 1


    fi


}
if [ -d ~/.aws ];then
    echo "seeting up the environment"
    setup $1 $2 $3
 else
     echo "direcorty is not there hence creating it"
     mkdir ~/.aws
     setup $1 $2 $3
fi

setupEc2DynamicInventory
exportData $1 $2
