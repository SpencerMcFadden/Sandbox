import json
import urllib2

url = "http://www.reddit.com/r/todayilearned/new.json?sort=new"

data = json.load(urllib2.urlopen(url))
front = data["data"]["children"]

conditions = {"TIL": "", "TIL,": "", "-": "", "Til": "", "til": "", "TIL that": ""}
conditions = dict((re.escape(k), v) for k, v in conditions.iteritems())
pattern = re.compile("|".join(conditions.keys()))

for i in xrange(0, len(front)-1):
    title = front[i]["data"]["title"].encode("utf-8")
    title = pattern.sub(lambda m: conditions[re.escape(m.group(0))], title)
    posts.append(title+"\n")

for text in posts:
    print(text)
