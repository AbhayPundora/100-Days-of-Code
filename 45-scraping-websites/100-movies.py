from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
contents = response.text


soup = BeautifulSoup(contents, "lxml")

movie_titles_tags = soup.find_all(name="h3", class_="title")

titles = [tag.getText() for tag in movie_titles_tags]
print(titles)

arranged_titles = titles[: : -1]
print(arranged_titles)

with open("movies.txt", mode="w",  encoding="utf-8") as file:
    for title in arranged_titles:
        file.write(f"{title}\n")

