import datetime

import pytest

from ... import app

AWS_REGION = "us-east-1"
SQS_QUEUE = "arn:aws:sqs:us-east-1:931066906971:iot-dynamodb-IotDemoQueue-PBICA74HO9GA"
TABLE_NAME = "iot-dynamodb-IotDemoTable-1N4QFAHEDD96E"
date_time = datetime.date


@pytest.fixture()
def post_event():
    """ Generates API GW Event"""
    post_body = "{\"TableName\":\"" + TABLE_NAME + "\",\"Item\":{\"date\": " + \
                "{\"S\": \"2000-01-01\"}, \"time\": {\"S\": \"06:45:43\"},\"location\": {\"S\": \"lab-5\"}, " + \
                "\"source\": {\"S\":\"wireless\"}, \"local_dest\": {\"S\": \"router-1\"}, \"local_avg\": " + \
                "{\"N\": \"5.32\"}, \"remote_dest\": {\"S\": \"device-1\"}, \"remote_avg\": {\"N\": \"11.01\"}}}"
    return {
        "Records": [
            {
                "body": post_body,
                "messageAttributes": {
                    "Method": {
                        "stringValue": "POST",
                        "stringListValues": [],
                        "binaryListValues": [],
                        "dataType": "String"
                    },
                    "eventSource": "aws:sqs",
                    "eventSourceARN": SQS_QUEUE,
                    "awsRegion": AWS_REGION
                }
            }
        ]
    }


@pytest.fixture()
def put_event():
    """ Generates API GW Event"""
    put_body = "{\"TableName\": \"" + TABLE_NAME + "\", " + \
               "\"Key\": {\"date\": {\"S\": \"2000-01-01\"},\"time\": {\"S\": \"06:45:43\"}}, " + \
               "\"UpdateExpression\": \"set remote_avg = :val1\", " + \
               "\"ExpressionAttributeValues\": {\":val1\": {\"N\": \"9.00\"}}}"
    return {
        "Records": [
            {
                "body": put_body,
                "messageAttributes": {
                    "Method": {
                        "stringValue": "PUT",
                        "stringListValues": [],
                        "binaryListValues": [],
                        "dataType": "String"
                    },
                    "eventSource": "aws:sqs",
                    "eventSourceARN": SQS_QUEUE,
                    "awsRegion": AWS_REGION
                }
            }
        ]
    }


@pytest.fixture()
def delete_event():
    """ Generates API GW Event"""
    delete_body = "{\"TableName\": \"iot-dynamodb-IotDemoTable-1N4QFAHEDD96E\", " + \
                  "\"Key\": {\"date\": {\"S\": \"2000-01-01\"}, \"time\": {\"S\": \"06:45:43\"}}}"
    return {
        "Records": [
            {
                "body": delete_body,
                "messageAttributes": {
                    "Method": {
                        "stringValue": "DELETE",
                        "stringListValues": [],
                        "binaryListValues": [],
                        "dataType": "String"
                    },
                    "eventSource": "aws:sqs",
                    "eventSourceARN": SQS_QUEUE,
                    "awsRegion": AWS_REGION
                }
            }
        ]
    }


def test_lambda_handler_post(post_event):
    ret = app.lambda_handler(post_event, None)
    assert ret == 0


def test_lambda_handler_put(put_event):
    ret = app.lambda_handler(put_event, None)
    assert ret == 0


def test_lambda_handler_delete(delete_event):
    ret = app.lambda_handler(delete_event, None)
    assert ret == 0
