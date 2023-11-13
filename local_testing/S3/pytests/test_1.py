import boto3
import pytest
from moto import mock_s3
from .. import test_1

# Using mock_ec2 as an example
@pytest.fixture
def mock_vpc_environment(monkeypatch):
    with mock_ec2():
        yield
@pytest.fixture
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    boto3.setup_default_session(aws_access_key_id="test", aws_secret_access_key="test", region_name="us-east-1")

@pytest.fixture
def s3_client(aws_credentials):
    with mock_s3():
        yield boto3.client('s3', region_name='us-east-1')

def test_create_s3_bucket(s3_client):
    # Define the bucket name for testing
    test_bucket_name = 'my-test-bucket'

    # Call the function to create the bucket
    create_s3_bucket(test_bucket_name)

    # Verify the bucket was created
    created_buckets = test_1.create_s3_bucket().list_buckets()['Buckets']
    assert any(bucket['Name'] == test_bucket_name for bucket in created_buckets)