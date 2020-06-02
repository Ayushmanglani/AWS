from __future__ import print_function

import json
import urllib
import boto3

from uuid import uuid4
def lambda_handler(event, context):
    s3 = boto3.client("s3")
    # bucket = event['Records'][0]['s3']['bucket']['name']
    sns = boto3.client('sns')
    sns.publish(
        TopicArn='arn:aws:sns:us-east-1:298671723150:Default_CloudWatch_Alarms_Topic',
        Subject='Object Upload',
        Message='Object Uploaded in s3 Bucket successfully'
    )
