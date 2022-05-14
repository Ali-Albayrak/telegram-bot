import re
import requests
import urllib.request

link = "https://web.facebook.com/watch/?v=2917664068342939"

html = requests.get(link)

print(re.search('sd_src:"(.+?)"', html.text))
try:
    url = re.search('hd_src:"(.+?)"', html.text)[1]

except:
    url = re.search('sd_src:"(.+?)"', html.text)[1]

print("started...")
urllib.request.urlretrieve(url,"test3.mp4")
print("done")
