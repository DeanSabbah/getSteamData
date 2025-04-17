import json
import random
import string

publishers = []
with open("result.json", "r", encoding="utf8") as data:
    dataList = json.load(data)
n=0
while n < len(dataList):
    #print(dataList[n])
    out = dataList[n]["publisher"].split(", ")
    x=0
    for pub in out:
        print(out[x])
        if not any (out[x] == name["name"] for name in publishers):
            characters = string.ascii_letters + string.digits + string.punctuation
            publishers.append({"name":out[x], "upcoming":[], "isPub":True, "password":''.join(random.choice(characters) for i in range(12))})
        x+=1
    n+=1

with open('resultPublishers.json', 'w') as fp:
    json.dump(publishers, fp)