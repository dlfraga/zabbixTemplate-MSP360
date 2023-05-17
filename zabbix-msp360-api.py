#!/usr/bin/env python3.10
import requests, sys

# loads local configuration from current path
import config

# Code taken from https://help.mspbackups.com/mbs-api-specification
authenticationRequest = requests.post(
    "https://api.mspbackups.com/api/Provider/Login",
    json={"UserName": config.apiUser, "Password": config.apiPassword},
)

if authenticationRequest.status_code == 403:
    print({"Error": "Authentication error, check credentials"})
    exit(1)
elif authenticationRequest.status_code == 200:
    access_token = authenticationRequest.json()["access_token"]
    ##
    # checks if the script was called with a parameter
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        # we assume that the parameter is a USERID and pass it to the API. We will return only the plans in that user id
        monitoringData = requests.get(
            "https://api.mspbackups.com/api/Monitoring/" + arg,
            headers={
                "Authorization": "Bearer " + access_token,
                "Accept": "application/json",
            },
        )
    else:
        # get monitoring data for the LLD rule
        monitoringData = requests.get(
            "https://api.mspbackups.com/api/Monitoring",
            headers={
                "Authorization": "Bearer " + access_token,
                "Accept": "application/json",
            },
        )

    if monitoringData.status_code == 200:
        print(monitoringData.text)
    else:
        print({"API acccess error": monitoringData.status_code})


else:
    print(
        {
            "Error": "Unknown error - return code different than 200 ok or 403 credential error."
        }
    )
    exit(1)
