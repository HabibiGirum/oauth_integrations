# replace these with accutal values
import requests
client_id = 'your client id'
client_secret = 'your client secret'
redirect_uri = 'your redirect uri'
authorization_code = "your code from redirect uri"

# supabase OAuth2.0 token endpoint
token_url = "https://api.supabase.com/v1/oauth/token"
# prepare the payload for the token request
payload = {
    "client_id": client_id,
    "client_secret": client_secret,
    "grant_type": "authorization_code",
    "redirect_uri": redirect_uri,
    "code": authorization_code,
}

# Make the POST request to get the access token
response = requests.post(token_url, data= payload)
#check if the request was seccessfull 
if requests.status_codes == 200:
    token_data = response.json()
    access_token = token_data.get("access_token")
    refresh_token= token_data.get("refresh_token")
    print("access token: ", access_token)
    print("refresh token:", refresh_token)
    
else:
    print("Failed to retrieve access token.")
    print("status code:", response.status_code)
    print("response:", response.text)
# to get client id and client secret go to 
# https://supabase.com/dashboard/org/gosnjbwboatjtgeqlspm/apps  

# the authorized url is 
# https://api.supabase.com/v1/oauth/authorize?client_id=your-client-id&redirect_uri=your-redirect-uri&response_type=code&scope=read  