import requests
import boto3
import base64
from botocore.exceptions import ClientError
import json

class autotaskAuth:
    def __init__(self, baseurl, username, password, integrationcode):
        
        self.baseurl = baseurl
        self.username = username
        self.password = password
        self.apiintegrationcode = integrationcode

        self.headers = {
            "Username": self.username,
            "Secret": self.password,
            "APIIntegrationcode": self.apiintegrationcode
        }

def loadAuthFromAWSSecrets():

    secret_name = "AutotaskAPI"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'DecryptionFailureException':
            # Secrets Manager can't decrypt the protected secret text using the provided KMS key.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InternalServiceErrorException':
            # An error occurred on the server side.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            # You provided an invalid value for a parameter.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            # You provided a parameter value that is not valid for the current state of the resource.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
        elif e.response['Error']['Code'] == 'ResourceNotFoundException':
            # We can't find the resource that you asked for.
            # Deal with the exception here, and/or rethrow at your discretion.
            raise e
    else:
        # Decrypts secret using the associated KMS key.
        # Depending on whether the secret is a string or binary, one of these fields will be populated.
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
            secrets = json.loads(secret)
        else:
            decoded_binary_secret = base64.b64decode(get_secret_value_response['SecretBinary'])
            
    # Your code goes here. 
    ATapiusername = secrets["ATapiusername"]
    ATapipassword = secrets["ATapipassword"]
    ATapiintegrationcode = secrets["ATapiintegrationcode"]
    ATbaseURL = secrets["ATbaseURL"]

    return autotaskAuth(ATbaseURL, ATapiusername, ATapipassword, ATapiintegrationcode)