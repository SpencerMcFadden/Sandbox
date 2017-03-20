import json
import urllib2

url = "https://www.reddit.com/r/todayilearned/new/.json"

data = json.load(urllib2.readurl(url))

print(data)
