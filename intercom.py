import requests

# Replace these with your actual values
client_id = "**"
client_secret = "**"
redirect_uri = "https://app.vistar.cloud/redirects/intercom"
authorization_code = "ZTgzMGYxMjEwYjhjNDY1NmIxMjM3OTgxNmVmZmJjMTI6dXMtZWFzdC0x"

# Intercom token endpoint
token_url = "https://api.intercom.io/auth/eagle/token"

# Prepare the payload
payload = {
    "code": authorization_code,
    "client_id": client_id,
    "client_secret": client_secret,
    "redirect_uri": redirect_uri,
    "grant_type": "authorization_code",
}

# Make the POST request
response = requests.post(token_url, data=payload)

# Check if the request was successful
if response.status_code == 200:
    token_data = response.json()
    print(token_data)
    access_token = token_data.get("access_token")
    refresh_token = token_data.get("refresh_token")
    print("Access Token:", access_token, "refresh_token:", refresh_token)
else:
    print("Failed to retrieve access token.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)