import requests  # Для запросов к URL
import random  # Shuffle
from bs4 import BeautifulSoup as b

URL = 'https://anekdotov.net/'  # Откуда


def parser(url):  # Функция парсинга с принимающим аргумент нужного Url
    r = requests.get(url)  # Берем нужный url
    soup = b(r.text, 'html.parser')  # передаем супчику взятый url и читаем из него текст
    anekdots = soup.find_all('div', class_='anekdot')  # суп найди все дивы с классом анекдот
    return [c.text for c in anekdots]  # Верни только текст из этих дивов в цикле


list_of_jokes = parser(URL)  # Список будет содержать ОТРЕТЁРНЕННЫЙ!!! текст без тэгов
random.shuffle(list_of_jokes)  # Перемешай список
print(list_of_jokes[0])  # Дай первое значение после шаффла.
print(random.choice(list_of_jokes))  # Или выбери без шаффла


#  https://www.crummy.com/software/BeautifulSoup/bs4/doc/ - Дока супа
#  https://egorovegor.ru/python-select-random-element/ - Статья рандома
