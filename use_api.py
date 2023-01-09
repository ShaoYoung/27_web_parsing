import requests
# Единственное, что нужно знать для начала работы с API — по какому URL-адресу его вызывать.
# https://api.twitter.com
# https://api.github.com
# https://api.stripe.com
# Как видите, перечисленные URL начинаются с https:// api. Не существует определенного стандарта, но чаще всего базовый URL следует этому шаблону.
# Попытавшись открыть любую из приведенных ссылок, вы заметите, что большинство из них возвращает ошибку или запрашивает учетные данные.
# Многие API-интерфейсы требуют аутентификации для определения прав доступа.

# случайный пользователь
url = 'https://randomuser.me/api/'
response = requests.get(url)
print(response.text)

# При вызове базового URL-адреса мы получаем сообщение, в котором говорится, что мы обратились к Dog API.
# Базовый URL здесь используется для получения информации об API, а не реальных данных.
url = 'https://api.thedogapi.com/'
response = requests.get(url)
print(response.text)
# Конечная точка (endpoint) — это часть URL-адреса, указывающая, какой ресурс мы хотим получить.
# Хорошо документированные API-интерфейсы содержат справочник по API, описывающий конечные точки и ресурсы API, а также способы их использования.
url = 'https://api.thedogapi.com/v1/breeds'
response = requests.get(url)
print(response.text)

# Все взаимодействия между клиентом (в нашем случае консолью Python) и API разделены на запрос (request) и ответ (response):
# request содержит данные запроса API: базовый URL, конечную точку, используемый метод, заголовки и т. д.
# response содержит соответствующие данные, возвращаемые сервером, в том числе контент, код состояния и заголовки.
print(response)
request = response.request
print(request)
print(request.url)
print(request.path_url)
print(request.method)
print(request.headers)

# Код состояния — одна из наиболее важных частей ответа API, которая сообщает,
# закончился ли запрос успешно, были ли найдены данные, нужна ли информация об учетной записи и т. д.
# Статус ответа можно проверить, используя .status_code и .reason. Библиотека requests также выводит код состояния в представлении Response-объекта
print(response.status_code)
print(response.reason)
# Чтобы проверить заголовки ответа, можно использовать response.headers
print(response.headers)
# Чтобы сделать то же самое с заголовками запроса, вы можно использовать response.request.headers, поскольку запрос является атрибутом объекта Response

# Еще один стандарт, с которым вы можете столкнуться при использовании API,— использование настраиваемых заголовков.
# Обычно они начинаются с префикса X-. Разработчики API обычно используют настраиваемые заголовки для отправки или запроса дополнительной информации от клиентов.
# Для определения заголовков можно использовать словарь, передаваемый в метод requests.get().
# Например, предположим, что вы хотите отправить некоторый идентификатор запроса на сервер API и знаете, что можете сделать это с помощью X-Request-Id
headers = {"X-Request-Id": "<my-request-id>"}
response = requests.get("https://example.org", headers=headers)
print(response.request.headers)
# X-Request-Id находится среди других заголовков, которые по умолчанию идут с любым запросом API

# Ответ обычно содержит множество заголовков, но один из наиболее важных — Content-Type. Этот заголовок определяет тип содержимого, возвращаемого в ответе.
# Чтобы правильно прочитать содержимое ответа в соответствии с различными заголовками Content-Type, объект Response поддерживает пару полезных атрибутов:
# .text возвращает содержание ответа в формате юникод.
# .content возвращает содержание ответа в виде байтовой строки.
# Мы уже использовали выше атрибут .text. Но для некоторых типов данных, таких как изображения и другие нетекстовые данные, обычно лучшим подходом использование .content.
# Для ответов API с типом содержимого application/json библиотека requests поддерживает специальный метод .json(),
# позволяющий получить представление данных в виде объекта Python:
# после выполнения response.json() мы получаем словарь, который можно использовать так же, как любой другой словарь в Python.

# При вызове API существует несколько различных методов, которые мы можем использовать, чтобы указать, какое действие хотим выполнить.
# Например, если мы хотим получить некоторые данные, мы используем метод GET, а если нужно создать некоторые данные — метод POST.
# HTTP-метод	Описание	Метод requests
# POST	Создает новый ресурс.	requests.post()
# GET	Считывает имеющийся ресурс.	requests.get()
# PUT	Обновляет существующий ресурс.	requests.put()
# DELETE	Удаляет ресурс.	requests.delete()
# До сих пор мы использовали только .get(), но мы можем использовать requests для всех прочих HTTP-методов:
# Большинство этих запросов вернут код состояния 405 (Method Not Allowed). Не все конечные точки поддерживают методы POST, PUT или DELETE.
# Действительно, большинство общедоступных API разрешают только запросы GET и не позволяют создавать или изменять существующие данные без авторизации.

# Параметры запроса
# Чтобы добавить параметр запроса к заданному URL-адресу, мы должны добавить вопросительный знак (?) перед первым параметром запроса.
# Если в запросе нужно указать несколько параметров, их разделяют с помощью амперсанда (&).
# Предположим, что мы хотим привлечь женскую аудиторию из Германии, и в качестве примеров необходимо сгенерировать соответствующих пользователей.
# Согласно документации, для нашей задачи можно использовать параметры запроса gender= и nat=
# requests.get("https://randomuser.me/api/?gender=female&nat=de").json()
# Чтобы избежать повторного создания URL-адреса, мы можем передавать параметры запроса в виде атрибута-словаря params
# query_params = {"gender": "female", "nat": "de"}
# requests.get("https://randomuser.me/api/", params=query_params).json()


endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
api_key = "DEMO_KEY"
query_params = {"api_key": api_key, "earth_date": "2020-07-01"}
response = requests.get(endpoint, params=query_params)
print(response.status_code)
# Возвращает содержимое ответа в формате json, если таковое имеется.
print(response.json())
# Мы используем .json() для преобразования ответа в словарь Python, затем извлекаем поле photos и получаем URL-адрес изображения для одной из фотографий.
# Если мы откроем URL в браузере, то увидим снимок Марса, сделанный марсоходом Curiosity
photos = response.json()['photos']
# print(photos)
for photo in photos:
    print(photo)
    # получаем ссылку по ключу 'img_src'
    print(photo['img_src'])




