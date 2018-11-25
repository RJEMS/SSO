# Code by Rajshree
# Performs oauth and connects to twitter using the client key and the secret key.
import oauth2

CLIENT_KEY = 'BcPXZRwvvcWCCMKU0tZsN2EGY'
CLIENT_SECRET = 'QwGSx6nFRYigJsszAGpZemDcgls1kp4otA3mEmsczwVi7u5y5J'
KEY = '1050660458254876672-xos6g6ejyVBVvOJVg88VarkIQ8PqF9'
SECRET = '2EPXVunPLsG6CQBBMBXh6AbTpmdC9LWr5MjDIaga2N0xz'


def oauth_req(url, http_method="GET", post_body=b'', http_headers=None):
    consumer = oauth2.Consumer(key=CLIENT_KEY, secret=CLIENT_SECRET)
    token = oauth2.Token(key=KEY, secret=SECRET)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers)
    return content


def oauth_post(url, http_method="POST", post_body=b'', http_headers=None):
    consumer = oauth2.Consumer(key=CLIENT_KEY, secret=CLIENT_SECRET)
    token = oauth2.Token(key=KEY, secret=SECRET)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers)
    return content