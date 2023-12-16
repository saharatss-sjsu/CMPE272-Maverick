#!/bin/bash

# This file use for running in EC2 instance user data

sudo apt update
sudo apt upgrade -y

sudo apt install python3-pip -y
sudo apt install python3-dev default-libmysqlclient-dev build-essential -y
sudo apt install libssl-dev -y
sudo apt install mysql-client-core-8.0 -y
sudo apt install pkg-config -y
sudo apt install unzip -y

export PROJECT_BASEPATH=/home/ubuntu
export PROJECT_DOWNLOAD=https://license-media.saharatss.org/server
export PROJECT_FILENAME=server_backend_t0ht676t5W4qpsaJPYwR.zip
export PROJECT_SERVICE_NAME=cmpe272_backend.service

cd $PROJECT_BASEPATH
wget $PROJECT_DOWNLOAD/$PROJECT_FILENAME
unzip $PROJECT_FILENAME
rm $PROJECT_FILENAME

cd CMPE281-P2-Backend
pip3 install -r setup/requirements.txt

touch run.sh
echo "
export DEBUG=False
python3 $PROJECT_BASEPATH/CMPE281-P2-Backend/manage.py runserver 0:8000
" > run.sh

cp setup/$PROJECT_SERVICE_NAME /etc/systemd/system/$PROJECT_SERVICE_NAME
sudo systemctl daemon-reload
sudo systemctl enable $PROJECT_SERVICE_NAME
sudo systemctl start $PROJECT_SERVICE_NAME

echo "Setup done!!"