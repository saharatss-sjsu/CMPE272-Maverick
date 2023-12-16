#!/bin/bash
cd $(dirname "$0")
cd ../..
zip -r CMPE272_Maverick-Client.zip CMPE272_Maverick -i \
	"CMPE272_Maverick/apps/*" \
	"CMPE272_Maverick/CMPE272_Maverick/*" \
	"CMPE272_Maverick/credentials/mysql.cnf" \
	"CMPE272_Maverick/setup/*.service" \
	"CMPE272_Maverick/setup/requirements.txt" \
	"CMPE272_Maverick/manage.py" \

