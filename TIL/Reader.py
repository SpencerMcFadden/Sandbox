import json
import urllib2

url = "http://www.reddit.com/r/todayilearned/new.json?sort=new"

data = json.load(urllib2.urlopen(url))
front = data["data"]["children"]

for i in xrange(0, len(front)-1):
    print(front[i]["data"]["title"].encode("utf-8").replace("TIL","")+"\n")
