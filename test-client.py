import requests
import sys


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


test_no_aws_auth()
