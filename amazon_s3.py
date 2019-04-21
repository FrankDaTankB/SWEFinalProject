import boto3
from botocore.exceptions import ClientError
import os

os.environ['AWS_DEFAULT_REGION'] = "us-east-1"

def checkBucketEncryption(aws_access_key_id, aws_secret_access_key):
    s3 = boto3.client('s3',
                      aws_access_key_id=accessKey,
                      aws_secret_access_key=secretKey,
                      )
    response = s3.list_buckets()
    for bucket in response['Buckets']:
        try:
            enc = s3.get_bucket_encryption(Bucket=bucket['Name'])
            print('Bucket: %s, Encryption: %s' % (bucket['Name'], rules))
        except ClientError as e:
            if e.response['Error']['Code'] == 'ServerSideEncryptionConfigurationNotFoundError':
                print('Bucket: %s, no server-side encryption' % (bucket['Name']))
            else:
                print("Bucket: %s, unexpected error: %s" % (bucket['Name'], e))
