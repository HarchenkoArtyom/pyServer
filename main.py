import google.oauth2.credentials
from flask import Flask, request
from google.oauth2 import id_token
from google.auth.transport import requests
app = Flask(__name__)


private_key_path = 'localhost.decrypted.key'
ssl_certificate_path = 'localhost.crt'


@app.route("/")
def hello():
    return "Hello World!"

@app.route('/login', methods=['POST'])
def login():
    try:
        credentials, project = google.auth.default()
        token = request.headers.get('idToken')
        email_r = request.headers.get('email')
        print(email_r)
        id_info = id_token.verify_oauth2_token(token, requests.Request())
        email = id_info['email']
        print(email)
        if(email == email_r):
            return 'true'
        else: return 'false';
        #return email
        #userid = idinfo['sub']
    except ValueError:
        print(ValueError)
        return 'false'

@app.route('/login2', methods=['POST'])
def login2():
    try:
        return 'true';
    except ValueError:
        print(ValueError)
        return 'false'


if __name__ == '__main__':
    """token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImEwNmFmMGI2OGEyMTE5ZDY5MmNhYzRhYmY0MTVmZjM3ODgxMzZmNjUiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI0MTIzNTA4NjMwMjctZGZpdGhnOGgwNjY4djFoNTJoOWhzcWY5NjAyazFyNDAuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI0MTIzNTA4NjMwMjctaWswODJpdDUyMTFhN2I1Y3VubGlwcjYzYm50aWxiZzguYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMDkzMzg0ODY2OTkxNTQ1NzY2NDUiLCJlbWFpbCI6Im5pa2l0YS5sZXZlbnRldjk3QGdtYWlsLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJuYW1lIjoiRXppbyBOaWsiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUNnOG9jTEZ3VkxZS2l3NnFiRjNTaFdNMXFrSUowSVRoLTUxbS00QmdGbHJzRVZOPXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6IkV6aW8iLCJmYW1pbHlfbmFtZSI6Ik5payIsImxvY2FsZSI6InJ1IiwiaWF0IjoxNjk4MDY5NDU2LCJleHAiOjE2OTgwNzMwNTZ9.eie_wFgBFYMpLHe9klHB3mDeP-eV1DEA3H3IvLtKouFNUSvycEoTT0Y2rDAvoAN0pMC4yfNKxHVNRqebhz5g06gScbhXCLxLHDZ-BT8mAKaqBOJWY9NCHXTgffnsFXnMK0nbHuwi8q03ARZaRszx6qo1pnxzSAYAqJEVnJMj2DPOTb1sYcb2aGQ7VAgVc9p03jv1oIgQDnkNI2Jqe16e45KERZ_9ypgIN7Ijm5sy7-aXn0mF4mqPu_oV38Xkg8Oa4YsiQMrIT_qidMrPFZeI41ldEk_Xf-504K-QfslmHDzkDg1vILVChlbl6SOLEI9MBBcJjPOUMNiG0XxUNtKtAw'
    t2='x1ZLpkPPIHU70LPxJgu9IkTSHVk2'
    credentials, project = google.auth.default()
    request = google.auth.transport.requests.Request()
    print(project)

    id_info = id_token.verify_oauth2_token(token, request)
    email = id_info['email'] ssl_context=ssl_context,
    print(email)"""
    #context = ('cert3.pem', 'key3.pem')
    app.run(ssl_context=('localhost.crt', 'localhost.decrypted.key'), host='0.0.0.0', port=8080)