# https://github.com/AndyTheFactory/newspaper4k

import json
from newspaper import Config
from newspaper import Article
from newspaper.utils import BeautifulSoup

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"

config = Config()
config.browser_user_agent = USER_AGENT
config.request_timeout = 10

base_url = 'https://www.bbc.com/travel/article/20241016-kamikochi-japans-car-free-town-that-autumn-hikers-love'
article = Article(base_url, config=config)
article.download()
article.parse()

meta_data_dict = article.meta_data
print(dict(meta_data_dict))

# for key, val in meta_data_dict.items():
#     if key == "description":
#         print(val)

# # ------------- parse using bs4 -----------
# soup = BeautifulSoup(article.html, 'html.parser')
# bbc_dictionary = json.loads("".join(soup.find("script", {"type":"application/ld+json"}).contents))
#
# date_published = [value for (key, value) in bbc_dictionary.items() if key == 'datePublished']
# print(date_published)
#
# article_author = [value['name'] for (key, value) in bbc_dictionary.items() if key == 'author']
# print(article_author)
#
# # another method to extract the title
# article_title = [value for (key, value) in bbc_dictionary.items() if key == 'headline']
# print(article_title)
