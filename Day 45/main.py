from bs4 import BeautifulSoup
import requests


# with open("Day 45\website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)


response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
anchors = soup.select(".titleline a")
# print(anchors)
for anchor in anchors:
    print(anchor.getText())
