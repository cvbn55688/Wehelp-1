import bs4
import urllib.request as req
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/movie/index.html"

nice = []
normal = []
bad = []

for i in range(10):
    print("page" + str(i+1))
    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    # print(data)
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title")
    for i in titles:
        if i.a != None:
            if i.a.string[0:4] == "[好雷]":
                nice.append(i.a.string)
            elif i.a.string[0:4] == "[普雷]":
                normal.append(i.a.string)
            elif i.a.string[0:4] == "[負雷]":
                bad.append(i.a.string)
            
    previousPage = root.find_all("a", class_="btn wide")[1]["href"]
    # print("https://www.ptt.cc" + previousPage)
    url = "https://www.ptt.cc" + previousPage

with open("movie.txt", "w", encoding="utf-8-sig") as file:
    for i in nice:
        file.write(i + "\n")
    for i in normal:
        file.write(i + "\n")
    for i in bad:
        file.write(i + "\n")
print("done")
