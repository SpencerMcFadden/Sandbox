import json
import urllib2

url = "http://www.reddit.com/r/todayilearned/new.json?sort=new"

data = json.load(urllib2.urlopen(url))

print(data)
