import requests

URL = "https://69.18.170.37:4443/php/rest/browse.php"

request = requests.get()
json = request.json()

print(json)