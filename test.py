import json
import requests

with open("result.json", "r", encoding="utf8") as data:
    dataList = json.load(data)


for n in range(len(dataList)):
    appid = dataList[n]["appid"]
    print(appid)
    try:
        request_api = requests.get("https://store.steampowered.com/api/appdetails?l=english&appids={}".format(appid))
        print("request 1:",request_api)
    except Exception as e:
        print(e)
    request_api = json.loads(request_api.text)
    dataList[n]["release_date"] = request_api["{}".format(appid)]["data"]["release_date"]["date"]
    dataList[n]["desc"] = request_api["{}".format(appid)]["data"]["short_description"]

with open('result.json', 'w') as fp:
    json.dump(dataList, fp)