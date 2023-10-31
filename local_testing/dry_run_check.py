import boto3

# Create an S3 client pointed at the LocalStack instance
s3 = boto3.client('s3', endpoint_url='http://localhost:4566')

# Example: List buckets
buckets = s3.list_buckets()
print(buckets)

ec2 = boto3.client('ec2', endpoint_url='http://localhost:4566')

try:
    response = ec2.start_instances(InstanceIds=['YOUR_INSTANCE_ID'], DryRun=True)
except ClientError as e:
    if 'DryRunOperation' not in str(e):
        print("You don't have permission to start instances.")
    else:
        print("You have permission to start instances.")