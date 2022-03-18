import pyautogui
import lyricsgenius
genius = lyricsgenius.Genius('7oRPoWKaH5gEgHLc-sxKp0C-vv5ouC2AW7XT-gxlIFyS9asH5X_jUpQpLef2Et-g')
genius.response_format = 'plain,html'
import time
import requests

res = genius.annotation
url = "https://api.genius.com/web_pages/lookup?canonical_url=https://api.genius.com/songs/378195"
request = requests.get(url)
json = request.json()

search_artist = {}
search_song = {}
artist = json.search_artist("Logic", max_songs=3, sort="title")
print(artist.songs)
song = json.search_song("44 More", artist.name)
print(song.lyrics)
