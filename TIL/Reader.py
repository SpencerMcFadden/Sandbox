import json
import urllib.request

url = "http://www.reddit.com/r/todayilearned/new.json?sort=new"

data = json.load(urllib.request.urlopen(url))

print(data)
