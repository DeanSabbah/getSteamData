import requests
import json
import time

result = {}

with open("notreleased.json", "r", encoding="utf8") as data:
    dataList = json.load(data)
with open("resultPublishers.json", "r", encoding="utf8") as pubData:
    pubList = json.load(pubData)

for game in dataList:
    print(game)
    request_api = requests.get("https://store.steampowered.com/api/appdetails?appids={}".format(game))
    print("request 1:",request_api)
    request_api_2 = requests.get("https://steamspy.com/api.php?request=appdetails&appid={}".format(game))
    print("request 2:",request_api_2)
    request_api = json.loads(request_api.text)
    request_api_2 = json.loads(request_api_2.text)
    timeInit = time.perf_counter()
    result[game] = {}
    print(result[game])
    result[game]["publishers"] = []
    for x in range(len(request_api[game]["data"]["publishers"])):
        for n in range(len(pubList)):
            if request_api[game]["data"]["publishers"][x].split()[0] in pubList[n]["name"]:
                result[game]["appid"] = game
                result[game]["name"] = request_api[game]["data"]["name"]
                result[game]["publishers"].append(pubList[n]["name"])
                result[game]["price"] = 0
                result[game]["thumbnail"] = request_api[game]["data"]["header_image"]
                result[game]['desc'] = request_api[game]["data"]["short_description"]
                result[game]["genre"] = request_api_2["genre"]
                result[game]["tags"] = request_api_2["tags"]
                result[game]["release_date"] = request_api[game]["data"]["release_date"]["date"]
                result[game]["reviews"] = []
                result[game]["likes"] = 0
                print(result[game])

    timeTotal = time.perf_counter() - timeInit
    time.sleep((1-timeTotal))

with open('resultUpcoming.json', 'w') as fp:
    json.dump(result, fp)