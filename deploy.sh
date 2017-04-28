#!/usr/bin/env bash

zip app.zip app.py
aws configure set default.region us-west-2
aws configure set aws_access_key_id $AWSKEY
aws configure set aws_secret_access_key $AWSSECRETKEY
aws lambda update-function-code --function-name clarkePythonLambda --zip-file fileb://./app.zip