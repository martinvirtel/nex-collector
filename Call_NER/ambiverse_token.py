import requests

def get_token(client_id,client_secret):
    ambiverse_api_url= "https://api.ambiverse.com/oauth/token"
    data={"grant_type": "client_credentials", "client_id":client_id, "client_secret":client_secret}
    r = requests.post(ambiverse_api_url, data=data)
    ambiverse_token_output = r.json()
    ambiverse_token = ambiverse_token_output ['access_token']
    return ambiverse_token