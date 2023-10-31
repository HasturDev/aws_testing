# aws_testing
This is a small test that I am writing to determine a persons AWS capabilities

in order to use this file you should simply need to do these actions
1. Have docker, boto3, localstack, and Python 3.9 or higher installed on your system
2. docker build -t localstack-python-boto3 .
3. Either run docker run -it -e INSTANCE_ID=ANOTHER_INSTANCE_ID localstack-python-boto3 in order to override the instance_id with your own or modify the instance ID to a default you want and run docker run -it localstack-python-boto3

Once this is done the file should start up and run an instance of localstack and allow you to test someone. You'll need to add your own testing files which will require you to run the docker run -it -v /path/on/host:/path/in/container localstack-python-boto3
command when starting up this container. Please tell me what modifications you would like to see and I would be more than happy to put them in or change this repo to fit any other needs. 

Thank you for your time
