# парсинг запроса в гугл
from bs4 import BeautifulSoup
import requests

# https://www.google.com/search?q=%D0%BB%D1%8B%D0%B6%D0%B8&rlz=1C1ASUM_enRU1005RU1005&oq=&aqs=chrome.3.35i39i362l8.2053125574j0j15&sourceid=chrome&ie=UTF-8
base_url = 'https://www.google.com'
extra_url = '/search?q=лыжи'
# обманка для сайта, который защищается от атак ботов. якобы запрос от браузера, а не от бота (headers)
# headers = {
#     'User-Agent': 'Chrome'
# 'User-Agent': 'Mozilla/5.0 (Macintoch; Intel Mac OS X 10.15; rv:76.0) Gecko/20100101 Firefox/76.0'
# }

# response = requests.get(base_url + extra_url, headers=headers)
response = requests.get(base_url + extra_url)
html = response.text
# print(html)
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())
teg_a = soup.find_all('a')
print(teg_a)
