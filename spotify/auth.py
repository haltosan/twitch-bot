import requests

URL = "https://accounts.spotify.com/authorize?"

URI = "https://spotify.com"
ID = "e0e58a3c1faf41a198d28d5f70a38996"
SCOPE = "playlist-modify-public"


keys = ['client_id','redirect_uri','scope','response_type']
values = [ID,URI,SCOPE,'code']
PARAMS = {'client_id':ID,
          'redirect_uri':URI,
          'scope':SCOPE,
          'response_type':'code'}

#URI+=keys[0]+"="+values[0]

#for k in range(1,len(keys)):
#    URL+="&"+keys[k]+"="+values[k]

r = requests.get(url = URL, params = PARAMS)
print(r.url)

#data = r.json()

#print(data)
print("raw")
print(r.raw)
