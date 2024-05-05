from bs4 import BeautifulSoup
import requests

city = "kiel"
url = "https://www.google.com/search?q=wetter+kiel"
#url = "https://www.google.com/search?q=" + "wetter+" + city
#url = "https://www.wetter.com/wetter_aktuell/wettervorhersage/3_tagesvorhersage/deutschland/kiel/DE0005426.html"

result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

wetter = doc.find("span", id="wob_tm")

print(wetter)






#with open("dummy.html", "r") as f:
    #doc = BeautifulSoup(f, "html.parser")

#tag = doc.find_all("p")
#print(tag)