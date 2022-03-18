import requests

url = "https://www.iseecars.com/used-cars/used-tesla-for-sale#Location=66952&Radius=all&Make=Model+3&Condition=used&_t=a&maxResults=15&sort=BestDeal&sortOrder=desc&lfc_t0=MTU2Nzk2NzNDc2NQ%3D%3D"
html = requests.get(url).text

from bs4 import BeautifulSoup
soup = BeautifulSoup(html)
print(soup.li)

