# 下載網址資料
import json
import urllib.request as request

src = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"  # 這是json格式

with request.urlopen(src) as response:
    # data = response.read().decode
    data = json.load(response)  # 用JSON模組處理JSON資料格式

list = data["result"]["results"]

with open("data.csv", "w", encoding="utf-8-sig") as file:
    for i in range(len(list)):
        if int(list[i]["xpostDate"][0:4]) >= 2015:
            file.write(list[i]["stitle"]+ ",")
            file.write(list[i]["address"][5:8]+ ",")
            file.write(list[i]["longitude"]+ ",")
            file.write(list[i]["latitude"]+ ",")
            file.write(list[i]["file"].lower().split(".jpg")[0]+".jpg"+ "\n")

            

        

# "stitle" = 景點名
# "address" = 區域名
# "longitude"
# "latitude"
# "file"[0] = 圖檔