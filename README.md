## Introduction
Zabbix + MSP360: External script and template to monitor backup plans from MSP360

## Files
zabbix-msp360-api.py: The external zabbix script. It is used to authenticate on msp360 api and returns the JSON data from the monitoring endpoint.
config.py: This file has the API username and password and must be filled with your own login details.
Template-MSP360.yaml: Zabbix template.

## Requirements
1. Tested on python 3.10 (it may work on other versions);
2. Package python-requests;
3. Tested on zabbix LTS 6.0;
4. MSP360 api credentials.

## Installation
1. Download the repo;
2. Copy zabbix-msp360-api.py and config.py to the "externalscripts" folder on your zabbix server;
3. Edit config.py and set your login details;
4. Import the template Template-MSP360.yaml into zabbix web;
5. Apply the template to a host. Only a single host is needed since the template and script will monitor all plans returned by MSP360.

## General Guidelines
* The script downloads all monitoring data each time it runs, so it's recommended to run it only when needed. You can control this by setting the interval on the template (GetAllMSP360MonitorData item).


