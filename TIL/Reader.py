# Currently written/functioning in Python 2.7

import json
import urllib2
import re
import os.path

url = "http://www.reddit.com/r/todayilearned/new.json?sort=new"

websiteJsonData = json.load(urllib2.urlopen(url))
childrenAsPosts = websiteJsonData["data"]["children"]
posts = []

conditionsToRemove = {"TIL": "", "TIL,": "", "Til": "", "til": "", "TIL:": "",\
                "Til:": "", "til:": "", "-": ""}
conditionsToRemove = dict((re.escape(k), v) for k, v in conditionsToRemove.iteritems())
removalPattern = re.compile("|".join(conditionsToRemove.keys()))

def findFacts(apiFile):
    """Read titles of posts from url, remove unecessary words/word combinations"""
    for i in xrange(0, len(front)-1):
        titleOfPost = apiFile[i]["data"]["title"].encode("utf-8")
        titleOfPost = removalPattern.sub(lambda m: conditionsToRemove[re.escape(m.group(0))], titleOfPost)
        temp = titleOfPost.split(" ", 2)
        if temp[1] == "that":
            titleOfPost = titleOfPost.replace("that", "", 1)
        titleOfPost = titleOfPost.strip().capitalize()
        posts.append(titleOfPost+"\n\n")
    return posts

def removeDuplicates(endList):
    """Check the existing output file to filter out any duplicates from the list of posts"""
    removalList = []
    for text in endList:
        redFile = open("reader.txt", "r")
        if text in redFile.read(os.path.getsize("reader.txt")):
            removalList.append(text)
    redFile.close()
    endList = [line for line in endList if line not in removalList]
    return endList

def textFile(factList):
    """Using the filtered list, write the results to a text file"""
    with open("reader.txt", "a") as output:
        for text in factList:
            output.write(text)
    return output


posts = findFacts(front)
if os.path.isfile("reader.txt"):
    posts = removeDuplicates(posts)
textFile(posts)
