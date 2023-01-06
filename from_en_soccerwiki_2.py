from bs4 import BeautifulSoup
import requests

base_url = 'https://en.soccerwiki.org/'
extra_url = 'league.php?leagueid=28'
html = requests.get(base_url + extra_url).text
soup = BeautifulSoup(html, 'html.parser')
# table = soup.find_all('table', class_='table-custom table-roster')[1]
# запись через атрибуты. значений в списке может быть несколько
table = soup.find_all('table', attrs={'class': ['table-custom table-roster']})[1]
td_s = table.select('td.text-left:nth-child(2)')
clubs = []
for td in td_s:
    if td.find('a') != None:
        # в список значения атрибута href (т.е. ссылка)
        clubs.append(td.find('a').attrs['href'])
# print(clubs)
# словарь национальностей
all_nations = {}
num_of_clubs = 0
num_of_players = 0
for club_url in clubs:
    num_of_clubs += 1
    html_team = requests.get(base_url + club_url).text
    soup_team = BeautifulSoup(html_team, 'html.parser')
    table = soup_team.select_one('table', class_='table-custom table-roster dataTable no-footer')
    td_s = table.select('td.text-center:nth-child(2)')
    # print(td_s)
    for td in td_s:
        # получаем значение атрибута data-sort
        nation = td.attrs['data-sort']
        num_of_players += 1
        if nation in all_nations:
            all_nations[nation] += 1
        else:
            all_nations[nation] = 1
# делаем список из сортированного словаря национальностей, key - ключ сортировки через lambda
count_nations = sorted(all_nations.items(), key=lambda item: item[1], reverse=True)
print(count_nations)
print(f'Всего {num_of_players} игроков в АПЛ в {num_of_clubs} командах')
