from bs4 import BeautifulSoup


with open("Day 45\website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.title)
