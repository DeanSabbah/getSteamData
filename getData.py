import requests
import json

result = []
n = 0

with open("games.json", "r", encoding="utf8") as data:
    dataList = json.load(data)

for game in dataList:
    print(dataList[game]["appid"])
    request_api = requests.get("https://store.steampowered.com/api/appdetails?appids={}".format(dataList[game]["appid"]))
    print("request 1:",request_api)
    request_api_2 = requests.get("https://steamspy.com/api.php?request=appdetails&appid={}".format(dataList[game]["appid"]))
    print("request 2:",request_api_2)
    gameInfo = json.loads(request_api.text)
    result.append(dataList[game])
    print(result)
    result[n]["thumbnail"] = gameInfo[game]["data"]["header_image"]
    result[n]['desc'] = gameInfo[game]["data"]["short_description"]
    gameInfo = json.loads(request_api_2.text)
    result[n]["genre"] = gameInfo["genre"]
    result[n]["tags"] = gameInfo["tags"]
    result[n]["reviews"] = []
    print(result[n])
    n+=1
    
with open('result.json', 'w') as fp:
    json.dump(result, fp)