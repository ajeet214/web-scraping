# https://github.com/AndyTheFactory/newspaper4k

import json
from newspaper import Config
from newspaper import Article
from newspaper.utils import BeautifulSoup

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"

config = Config()
config.browser_user_agent = USER_AGENT
config.request_timeout = 10

base_url = 'https://edition.cnn.com/2025/08/13/travel/nepal-mountain-climbing-free-intl-hnk'
article = Article(base_url, config=config)
article.download()
article.parse()
print(article.title)
print(article.publish_date)
print(article.authors)

meta_data_dict = article.meta_data
print(dict(meta_data_dict))


