# replace these with accutal values
import requests
SUPABASE_CLIENT_ID = '92107096-93b9-4411-8fec-666759b05b32'
SUPABASE_CLIENT_SECRET = 'sba_694f39ba292899e64c03f98377e3deeecce0d672'
redirect_uri = 'https://app.vistar.cloud/redirects/supabase'
authorization_code = "c666b205-b77f-4b43-8f9d-5af014a1456a"
refresh_token = "WbRhxhxtRhgqIWUtcE"
data = {
            'grant_type': 'refresh_token',
            'client_id': SUPABASE_CLIENT_ID,
            'client_secret': SUPABASE_CLIENT_SECRET,
            'refresh_token': refresh_token
        }
# supabase OAuth2.0 token endpoint
token_url = "https://api.supabase.com/v1/oauth/token"
# prepare the payload for the token request
# payload = {
#     "client_id": client_id,
#     "client_secret": client_secret,
#     "grant_type": "authorization_code",
#     "redirect_uri": redirect_uri,
#     "code": authorization_code,
# }

# Make the POST request to get the access token
response = requests.post(token_url, data= data)
#check if the request was seccessfull 
if requests.status_codes == 200 or 201:
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