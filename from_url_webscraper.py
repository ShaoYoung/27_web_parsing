from bs4 import BeautifulSoup
import requests
import pandas as pd


def myfun(tag):
    # if tag.text.lower().find('vivobook') > -1:
    #     print(" ".join(tag.text.lower().split()))
    return tag.text.lower() == "asus vivobook x4..."
    # return tag.text.lower().find('vivobook') > -1


if __name__ == '__main__':
    url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
    response = requests.get(url)
    if response.ok:
        # print(response.text)
        soup = BeautifulSoup(response.text, 'lxml')
        print(soup.header.p.text)
        a_start = soup.header.a
        print(a_start)
        # доступ к атрибутам тега через .attrs. Получаем словарь
        print(a_start.attrs)
        print(a_start.attrs['data-target'])
        price = soup.find('h4', class_="pull-right price")
        print(f"Цена {price.text}")
        # найти все. на выходе list
        price = soup.find_all('h4', class_="pull-right price")
        print(price)
        # найти с 3 по 5, т.е. [2:5). на выходе list
        price = soup.find_all('h4', class_="pull-right price")[2:5]
        print(price)
        print("=================")

        # Filter by name (list)
        name = soup.find_all('a', class_='title')
        # for n in names:
        #     if n.text.lower().find('asus') > -1:
        #         print(n.text)
        # Filter by price (list)
        price = soup.find_all('h4', class_='pull-right price')
        # Filter by reviews (list)
        reviews = soup.find_all('p', class_='pull-right')
        # Filter by description (list)
        description = soup.find_all('p', class_='description')

        # tag = soup.find(myfun)
        # print("=======")
        # print(" ".join(tag.text.split()))

        # Create for loop to make string from find_all list
        product_name_list = []
        price_list = []
        review_list = []
        description_list = []
        for item in name:
            n = item.text
            product_name_list.append(n)
        for item in price:
            price = item.text
            price_list.append(price)
        for item in reviews:
            rev = item.text
            review_list.append(rev)
        for item in description:
            desc = item.text
            description_list.append(desc)

        for i in range(0, len(product_name_list)):
            print(
                f"Модель {product_name_list[i]} цена {price_list[i]} отзывов {review_list[i]} описание {description_list[i]}")

        # создание DataFrame
        table = pd.DataFrame({'Product Name': product_name_list, 'Price': price_list, 'Reviews': review_list,
                                  'Description': description_list})
        table.to_csv('notebooks.csv')
        # table.to_excel('notebooks.xlsx')
        # writer = pd.ExcelWriter('notebooks.xlsx')
        table.to_excel('notebooks.xlsx', sheet_name="Ноутбуки", startrow=2, startcol=2)
        # table.to_excel(writer)
        # writer.save()


