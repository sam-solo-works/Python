import pyautogui
import lyricsgenius
genius = lyricsgenius.Genius('7oRPoWKaH5gEgHLc-sxKp0C-vv5ouC2AW7XT-gxlIFyS9asH5X_jUpQpLef2Et-g')
genius.response_format = 'plain,html'
import time
import requests

#For help on this subject https://github.com/johnwmillr/LyricsGenius

res = genius.annotation
URL = "https://api.genius.com/web_pages/lookup?canonical_url=https://api.genius.com/songs/378195"
request = requests.get(url)
json = request.json()


#Annotation in plain formatting
print(res['annotation']['body']['plain'])

#Annotation in html formatting
#print(res['annotation']['body']['html'])

word = input("what word would you like to see:\n")
times = int(input("How many times would you like to see it:\n"))

for i in range(0,times):
    time.sleep(5)
    pyautogui.typewrite(word)
    pyautogui.typewrite("\n")
    i = i + 1
    times = (str(i))
    print (word, "#", times, "printed\n")