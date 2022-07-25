import requests
import sys

# Use aws-requests-auth from https://github.com/davidmuller/aws-requests-auth
# in a virtualenv in /tmp/v

hook_data = {
    "build_id": 5,
    "warning": "birds fly over the rainbow",
    "you_know_this_is_totally_made_up": 5  # True
}

def test_no_aws_auth():
    hook_url = f"http://{sys.argv[1]}:{sys.argv[2]}/api-gateway-hook"
    r = requests.post(hook_url, json=hook_data)
    print(r.status_code)
    print (r.text)

# See https://github.com/boto/botocore/issues/1784
def test_with_aws_auth():
    from aws_requests_auth.aws_auth import AWSRequestsAuth
    import boto3
    hook_url = sys.argv[1]
    profile_name = sys.argv[2]
    role_arn = sys.argv[3]
    hook_api_host =  "https://eq8hydgoha.execute-api.us-east-2.amazonaws.com/test-root".split("/")[2]
    sess = boto3.Session(profile_name=profile_name)

    creds = sess.client('sts').assume_role(RoleArn=role_arn, RoleSessionName='test')['Credentials']

    auth = AWSRequestsAuth(
        aws_access_key=creds['AccessKeyId'],
        aws_secret_access_key=creds['SecretAccessKey'],
        aws_token=creds['SessionToken'],
        aws_region='us-east-2',
        aws_service="execute-api",
        aws_host=hook_api_host
    )
    #auth = AWSRequestsAuth(aws_access_key=creds.access_key,aws_secret_access_key=creds.secret_key,aws_token=creds.token,aws_region='us-east-2',aws_service="execute-api",aws_host=hook_api_host)


    r = requests.post(hook_url, json={}, auth=auth)
    print(r.status_code)
    print (r.text)



if sys.argv[1][0:5] == 'https':  # In AWS
    test_with_aws_auth()
else:
    test_no_aws_auth()
