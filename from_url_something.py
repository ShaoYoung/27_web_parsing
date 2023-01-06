from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = "http://www.something.com"
    # Сессия запросов. Обеспечивает сохранение файлов cookie, пул соединений и настройку.
    new_session = requests.Session()
    response = new_session.get(url)
    # print(response)
    # print(type(response))
    if response.ok:
        # print(response.headers)
        # print(response.cookies)
        # print(f'Text {response.text}')
        # print(f'Тип {type(response.text)}')
        # print(f'Content {response.content}')
        # print(f'Тип {type(response.content)}')
        # # результат выполнения запроса (True/False)
        # print(response.ok)
        soup = BeautifulSoup(response.text, 'lxml')
        # тег title
        print(soup.title)
        # текст тега title
        print(soup.title.text)
        # родитель тега title
        print(soup.title.parent)
    else:
        print('Ошибка связи')
        quit()
    # При помощи метода prettify() можно добиться того, чтобы HTML-код выглядел аккуратнее
    # print(soup.prettify())


