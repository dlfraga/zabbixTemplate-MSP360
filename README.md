## Introduction
Zabbix + MSP360: External script and template to monitor backup plans from MSP360

## Files
zabbix-msp360-api.py: The external zabbix script. It is used to authenticate on msp360 api and returns the JSON data from the monitoring endpoint.
config.py: This file has the API username and password and must be filled with your own login details.

## General Guidelines
* The script downloads all monitoring data each time it runs, so it's recommended to run it only when needed
