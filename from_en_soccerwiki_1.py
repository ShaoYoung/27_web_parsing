# названия, тренеры, стадионы, местоположение клубов АПЛ
from bs4 import BeautifulSoup
import requests


def parse_table(table, col):
    # выбор указанных тегов с условием. на выходе список тегов
    # в данном случае выбираем второй тег (т.е. вторую колонку таблицы) с class=text-left
    td_s = table.select(f'td.text-left:nth-child({col})')
    # print(td_s)
    list_tab = []
    for td in td_s:
        if col < 5:
            # в каждом теге td ищем тег a и если он не None (первая строка), записываем text в список
            if td.find('a') != None:
                list_tab.append(td.find('a').text)
        else:
            # print(td)
            list_tab.append(td.text)
    if col == 5:
        list_tab.pop(0)
    return list_tab


url = 'https://en.soccerwiki.org/league.php?leagueid=28'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
# print(soup.prettify())
# print(soup.h1.name)
table = soup.find_all('table', class_='table-custom table-roster')[1]
clubs = parse_table(table, 2)
print(clubs)
managers = parse_table(table, 3)
print(managers)
stadiums = parse_table(table, 4)
print(stadiums)
locations = parse_table(table, 5)
print(locations)
