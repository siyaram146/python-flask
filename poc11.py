import boto3

sts_client = boto3.client('sts')

def aws_secret():
    """
    This function is to fetch the secrets from AWS secret manager
    """
    role_arn = 'arn:aws:iam::031405088851:role/poc-client-cred'
    assumed_role_object = sts_client.assume_role(RoleArn=role_arn, RoleSessionName='session1')
    credentials = assumed_role_object['Credentials']
    secrets_client = boto3.client(
        service_name='secretsmanager',
        region_name="us-east-2",
        aws_access_key_id=credentials['AccessKeyId'],
        aws_secret_access_key=credentials['SecretAccessKey'],
        aws_session_token=credentials['SessionToken']
    )
    secret_arn = 'arn:aws:secretsmanager:us-east-2:031405088851:secret:demo-access-key-Id6FeW'
    secrets = secrets_client.get_secret_value(SecretId=secret_arn).get('SecretString')
    secret_dict = json.loads(secrets)
    return secret_dict

demo = aws_secret()
print("aws value", demo)
