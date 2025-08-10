
from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.select(".titleline a")
upvotes = soup.find_all(name="span", class_="score")

article_texts = [article.getText() for article in articles]
article_links = [article.get("href") for article in articles]
article_upvotes = [int(upvote.getText().split(" ")[0]) for upvote in upvotes]

# print(article_texts)
# print(article_links)
print(article_upvotes)

max_score = max(article_upvotes)
max_index = article_upvotes.index(max_score)
print(max_index)

print(f"title: {article_texts[max_index]}")
print(f"link: {article_links[max_index]}")














































# with open("website.html") as html_file:
#     contents = html_file.read()
#
# # can use "html.parser" but for certain websites it will not work so use "lxml"
# soup = BeautifulSoup(contents, "lxml")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# #
# # print(soup) # basically our html document
# # print(soup.prettify()) # to make indents
# # soup.a  will give first anchor tag
#
# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     # print(tag.string)
#     print(tag.getText())
#     print(tag.get("href"))
#
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# print(soup.select(".heading"))