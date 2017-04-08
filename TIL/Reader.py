import json
import urllib2
import re
import os.path

url = "http://www.reddit.com/r/todayilearned/new.json?sort=new"

data = json.load(urllib2.urlopen(url))
front = data["data"]["children"]
posts = []

conditions = {"TIL": "", "TIL,": "", "Til": "", "til": "", "TIL:": "",\
                "Til:": "", "til:": "", "-": ""}
conditions = dict((re.escape(k), v) for k, v in conditions.iteritems())
pattern = re.compile("|".join(conditions.keys()))

def findFacts(apiFile):
    for i in xrange(0, len(front)-1):
        title = apiFile[i]["data"]["title"].encode("utf-8")
        title = pattern.sub(lambda m: conditions[re.escape(m.group(0))], title)
        temp = title.split(" ", 2)
        if temp[1] == "that":
            title = title.replace("that", "", 1)
        title = title.strip().capitalize()
        posts.append(title+"\n\n")
    return posts

def removeDuplicates(foundList):
    tempList = []
    for text in foundList:
        output = open("reader.txt", "r")
        if text in output.read(os.path.getsize("reader.txt")):
            tempList.append(text)
    output.close()
    foundList = [line for line in foundList if line not in tempList]
    return foundList

def textFile(factList):
    with open("reader.txt", "a") as output:
        for text in factList:
            output.write(text)
    return output


posts = findFacts(front)
if os.path.isfile("reader.txt"):
    posts = removeDuplicates(posts)
textFile(posts)
