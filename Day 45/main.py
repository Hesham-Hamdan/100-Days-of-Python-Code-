from bs4 import BeautifulSoup
import requests


# with open("Day 45\website.html") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)


# response = requests.get("https://news.ycombinator.com/news")
# yc_webpage = response.text

# soup = BeautifulSoup(yc_webpage, "html.parser")
# anchors = soup.select(".titleline a")
# # print(anchors)
# for anchor in anchors:
#     print(anchor.getText())

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.get(
    "https://empireonline.com/movies/features/best-movies-2", headers=headers
)
empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, "html.parser")
titles = soup.select(".content_content__i0P3p h2 strong")

names = []
for title in titles:
    text = title.getText()
    if ")" in text:
        names.append(text)

names.reverse()
with open("Day 45\movies.txt", "w") as file:
    for name in names:
        file.write(f"{name}\n")
