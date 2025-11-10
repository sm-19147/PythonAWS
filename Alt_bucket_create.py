import logging
import boto3
from botocore.exceptions import ClientError


def create_bucket(bucket_name, region):
    """Create an S3 bucket in a specified region

    If a region is not specified, the bucket is created in the S3 default
    region (us-east-1). 

    :param bucket_name: Bucket to create
    :param region: String region to create bucket in, e.g., 'us-west-2'
    :return: True if bucket created, else False
    """

    # Create bucket

    try:
        bucket_config = {}
        s3_client = boto3.client('s3', region)
        if region != 'us-east-1':
            bucket_config['CreateBucketConfiguration'] = {'LocationConstraint': region}

        s3_client.create_bucket(Bucket='nicebucket19599',**bucket_config) #Edit the bucket name here
    except ClientError as e:
        logging.error(e)
        return False
    return True
create_bucket('thisisauniquebucketname22180','us-east-1')

response = boto3.client('s3').create_bucket(
    Bucket='yetanotherboto3bucket123456',
)

print(response)