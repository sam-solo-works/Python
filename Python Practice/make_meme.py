import requests


url = "https://api.imgflip.com/get_memes"
request = requests.get(url)
json = request.json()

user_req = input("meme?")
for 
memes = json.get("data").get("memes")[1].get("name")
#print(memes)