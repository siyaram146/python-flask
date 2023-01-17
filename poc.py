import json
import boto3

demo = aws_secret()
print("aws value", demo)
def aws_secret():
    """
    This function is to fetch the secrets from AWS secret manager
    """
    secrets_client = boto3.client(
        service_name='secretsmanager',
        region_name="us-east-2")
    secret_arn = 'arn:aws:secretsmanager:us-east-2:031405088851:secret:demo-access-key-Id6FeW'
    secrets = secrets_client.get_secret_value(SecretId=secret_arn).get('SecretString')
    secret_dict = json.loads(secrets)
    return secret_dict
    