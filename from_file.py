from bs4 import BeautifulSoup
import re


def myfun(tag):
    # проверка на пустой тег. возврат bool
    return tag.is_empty_element


if __name__ == '__main__':

    filename = "index.html"
    with open(filename, "r") as f:
        content = f.read()
    # print(content)
    # объект BeautifulSoup.
    # Первый параметр строка или файловый объект, который будем парсить.
    # Второй параметр - функция парсера (имя парсера или используемый тип разметки) рекомендуется указывать конкретный синтаксический анализатор
    soup = BeautifulSoup(content, 'html.parser')
    # soup = BeautifulSoup(content, 'lxml')
    # выводим определённые теги и их содержимое
    print(soup.h2)
    print(soup.head)
    print(soup.li)
    print(f"HTML: {soup.h2}, имя тега - {soup.h2.name}, текст в теге - {soup.h2.text}")
    # перебор всех тегов - метод recursiveChildGenerator
    for tag in soup.recursiveChildGenerator():
        if tag.name:
            print(tag.name)
    # записываем в root (корень) - тег html
    root = soup.html
    print(root.name)
    # при помощи атрибута тега children можно вывести все дочерние теги. Например, здесь у тега html два дочерних тега HEAD и BODY
    root_childs = [e.name for e in root.children if e.name is not None]
    print(root_childs)
    # При помощи атрибута тега descendants можно получить список всех потомков (дочерних элементов всех уровней) рассматриваемого тега
    root = soup.body
    root_childs = [e.name for e in root.descendants if e.name is not None]
    # Данный пример позволяет найти всех потомков главного тега body
    print(root_childs)

    # При помощи метода find() можно найти элементы страницы, используя различные опорные параметры, в том числе id. Находит первый элемент.
    # Находит первый тег ul, у которого аттрибут id равен mylist. Строка в комментарии является альтернативным способом выполнить то же самое задание.
    # print(soup.find("ul", attrs={ "id" : "mylist"}))
    print(soup.find("ul", id="mylist"))

    # При помощи метода find_all() можно найти все элементы, которые соответствуют заданным критериям. Возвращает list
    for tag in soup.find_all("li", style="width:150px"):
        print(f"{tag.name} : {tag.text}")

    # Метод find_all() также при поиске использует список из названий тегов.
    # В данном примере показано, как найти все теги h2 и p, после чего вывести их содержимое на экран.
    tags = soup.find_all(['h2', 'p'])
    for tag in tags:
        # print(tag.text)
        print(" ".join(tag.text.split()))

    # Метод find_all() также может использовать функцию, которая определяет, какие элементы должны быть выведены.
    tags_2 = soup.find_all(myfun)
    # Данный пример выводит пустые элементы.
    print(tags_2)

    # Также можно найти запрашиваемые элементы, используя регулярные выражения.
    strings = soup.find_all(string=re.compile(r'\d+'))
    for txt in strings:
        print(" ".join(txt.split()))

    # При помощи методов select() и select_one() для нахождения запрашиваемых элементов можно использовать некоторые CSS селекторы
    # В данном примере используется CSS селектор, который выводит на экран HTML-код третьего по счету элемента li.
    print(soup.select("li:nth-of-type(3)"))

    # В CSS символ # используется для выбора тегов по их id-атрибутам
    # В данном примере выводятся элементы, которых есть id под названием mylist
    print(soup.select_one("#mylist"))

    # Метод append() добавляет в рассматриваемый HTML-документ новый тег
    # Для начала, требуется создать новый тег при помощи метода new_tag().
    newtag = soup.new_tag('li')
    # и его содержимое
    newtag.string = 'Новый тег'
    # Далее создается сноска на тег ul
    # ultag = soup.ul
    # ultag.append(newtag)
    # аналогично
    soup.ul.append(newtag)
    # print(ultag.prettify())

    # Метод insert() позволяет вставить тег в определенно выбранное место.
    newtag = soup.new_tag('li')
    newtag.string = 'Новый тег в определённое место'
    ultag = soup.ul
    ultag.insert(3, newtag)

    # Метод replace_with() заменяет содержимое выбранного элемента.
    tag = soup.find(text="Windows10")
    # print(tag.text)
    # В примере показано, как при помощи метода find() найти определенный элемент, а затем, используя метод replace_with(), заменить его содержимое.
    tag.replace_with('Виндоуз10')

    # Метод decompose() удаляет определенный тег из структуры документа и уничтожает его.
    ptag2 = soup.select_one("p:nth-of-type(2)")
    # В данном примере показано, как удалить второй элемент p в документе.
    ptag2.decompose()

    print(soup)



