import json
import urllib2
import re

url = "http://www.reddit.com/r/todayilearned/new.json?sort=new"

data = json.load(urllib2.urlopen(url))
front = data["data"]["children"]
posts = []

conditions = {"TIL": "", "TIL,": "", "Til": "", "til": "", "TIL:": "", "Til:": "",\
                "til:": "", "-": ""}
conditions = dict((re.escape(k), v) for k, v in conditions.iteritems())
pattern = re.compile("|".join(conditions.keys()))

for i in xrange(0, len(front)-1):
    title = front[i]["data"]["title"].encode("utf-8")
    title = pattern.sub(lambda m: conditions[re.escape(m.group(0))], title)
    temp = title.split(" ", 2)
    if temp[1] == "that":
        title = title.replace("that", "", 1)
    title = title.strip().capitalize()
    posts.append(title+"\n")

for text in posts:
    with open("reader.txt", "a") as output:
        output.write(text)
        output.close()
