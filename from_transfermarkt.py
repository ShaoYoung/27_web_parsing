# все игроки, забывавшие мячи в лиге чемпионов 2022 года
from bs4 import BeautifulSoup
import requests

base_url = 'https://www.transfermarkt.com'
extra_url = '/uefa-champions-league/torschuetzenliste/pokalwettbewerb/CL/saison_is/2022'
# обманка для сайта, который защищается от атак ботов. якобы запрос от браузера, а не от бота (headers)
headers = {
    'User-Agent': 'Chrome'
    # 'User-Agent': 'Mozilla/5.0 (Macintoch; Intel Mac OS X 10.15; rv:76.0) Gecko/20100101 Firefox/76.0'
}
rating = []
count_of_goals = 0
flag = True
while flag:
    response = requests.get(base_url + extra_url, headers=headers)
    html = response.text
    # print(response.status_code)

    html_rating = BeautifulSoup(html, 'html.parser')
    # выбор: тег div с классом pager, далее тег li с классом tm-pagination__list-item -> тег a
    # next_page = html_rating.select_one('div.pager li.tm-pagination__list-item tm-pagination__list-item--icon-next-page a')
    # <li class="tm-pagination__list-item tm-pagination__list-item--icon-next-page"><a href="/uefa-champions-league/torschuetzenliste/pokalwettbewerb/CL/ajax/yw1/saison_is/2022/page/2" title="Go to next page" class="tm-pagination__link">&nbsp;&nbsp;</a></li>
    # почему-то не сработал

    li_next_page = html_rating.find('li', class_='tm-pagination__list-item tm-pagination__list-item--icon-next-page')
    # print(li_next_page)
    # если есть кнопка "next page", то берём ссылку на неё из атрибута href и делаем добавочный url, иначе завершение цикла на текущей странице
    if li_next_page != None:
        extra_url = li_next_page.select_one('a').attrs['href']
        # print(extra_url)
    else:
        flag = False
    # находим div, внутри которого нужная таблица
    div = html_rating.find('div', class_='responsive-table')
    # print(div)
    # находим нужную таблицу
    table = div.find('table', class_='items')
    # print(table)
    # находим нужное tbody
    tbody = table.find('tbody')
    # print(tbody)
    # в каждой строке таблицы (tr) берём последний столбец (td), причём проваливаемся внутрь каждой строки (tr)
    # players = tbody.select('tr > td:last-child')
    # print(players)
    # print('===')
    # или можно через поиск всех тегов td, где class = zentriert hauptlink
    zen = tbody.find_all('td', class_='zentriert hauptlink')
    # print(zen)
    for player in zen:
        a = player.select_one('a')
        name = a.attrs['title']
        goalscore = int(a.text)
        count_of_goals += goalscore
        rating.append((name, goalscore))
        # print('=========')
print(rating)
print(f'Кол-во игроков, забивавших мячи - {len(rating)}')
print(f'Всего забито мячей - {count_of_goals}')

# смотреть пэйджинатор, в частности последнюю страницу и её href
# индивидуально для каждого сайта
# со временем теги и их потроха меняются
