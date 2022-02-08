import datetime
import json

import requests  # для URL запроса
from bs4 import BeautifulSoup  # для работы с HTML
import time  # для установки задержки в цикле программы
box = {
    'gazp1' : {
        'adress': "https://www.google.com/finance/quote/GAZP:MCX?sa=X&ved=2ahUKEwjK5-z-yJLyAhUhpIsKHXbMBh0Q_AUoAXoECAEQAw",
        'class': "YMlKec fxKbKc"
    },
    'gazp' : {
        'adress': "https://ru.investing.com/equities/gazprom_rts",
        'class': "text-2xl",'data-test':'instrument-price-last'
    },
    'mmk' : {
        'adress': "https://ru.investing.com/equities/mmk_rts",
        'class': "text-2xl",'data-test':'instrument-price-last'
    },
    'sber' : {
        'adress': "https://ru.investing.com/equities/sberbank_rts",
        'class': "text-2xl','data-test':'instrument-price-last"
    }
}
sleep = 3  # время задержки
def ticker(adress):
    # ссылка на тикер (Я использовал сайт google finance)
    #GAZP = "https://www.google.com/finance/quote/GAZP:MCX?sa=X&ved=2ahUKEwjK5-z-yJLyAhUhpIsKHXbMBh0Q_AUoAXoECAEQAw"
    # заголовки для URL запроса.(добавляется к ссылке при URL запросе)
    headers = {
        'user agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/97.0.4692.99 Safari/537.36"}
    # запрашиваем страницу по ссылке и помещаем в переменную html
    html = requests.get(adress, headers)
    # парсим данные в переменную soup
    soup = BeautifulSoup(html.content, 'html.parser')
    # находим интересующий нас тэг с текущей ценой акции
    # (В браузере используем просмотр кода элемента для того чтобы найти это значение)
    convert = soup.findAll('span', {'class': 'text-2xl','data-test':'instrument-price-last'})
    # считываем 1й элемент как текст.
    # Делаем срез и избавляемся от знака ₽ в начале строки,
    # конвертируем строку в число типа float
    price = convert[0].text

    # print("Цена акции Газпром: ", price)
    return price
    # time.sleep(sleep)
    # update_ticker_GAZP()  # вызываем эту же функцию снова


def update_ticker_GAZP():
    # ссылка на тикер (Я использовал сайт google finance)
    GAZP = "https://www.google.com/finance/quote/GAZP:MCX?sa=X&ved=2ahUKEwjK5-z-yJLyAhUhpIsKHXbMBh0Q_AUoAXoECAEQAw"
    # заголовки для URL запроса.(добавляется к ссылке при URL запросе)
    headers = {
    'user agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/97.0.4692.99 Safari/537.36"}
    # запрашиваем страницу по ссылке и помещаем в переменную html
    html = requests.get(GAZP, headers)
    # парсим данные в переменную soup
    soup = BeautifulSoup(html.content, 'html.parser')
    # находим интересующий нас тэг с текущей ценой акции
    # (В браузере используем просмотр кода элемента для того чтобы найти это значение)
    convert = soup.findAll('div', {'class': 'YMlKec fxKbKc'})
    # считываем 1й элемент как текст.
    # Делаем срез и избавляемся от знака ₽ в начале строки,
    # конвертируем строку в число типа float
    price = float(convert[0].text[1:])

    #print("Цена акции Газпром: ", price)
    return price
    #time.sleep(sleep)
    #update_ticker_GAZP()  # вызываем эту же функцию снова

def update_ticker_SBER():
    # ссылка на тикер (Я использовал сайт google finance)
    GAZP = "https://ru.investing.com/equities/sberbank_rts"
    # заголовки для URL запроса.(добавляется к ссылке при URL запросе)
    headers = {
        'user agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/97.0.4692.99 Safari/537.36"}
    # запрашиваем страницу по ссылке и помещаем в переменную html
    html = requests.get(GAZP, headers)
    # парсим данные в переменную soup
    soup = BeautifulSoup(html.content, 'html.parser')
    # находим интересующий нас тэг с текущей ценой акции
    # (В браузере используем просмотр кода элемента для того чтобы найти это значение)
    convert = soup.findAll('span', {'class': 'text-2xl','data-test':'instrument-price-last'})
    # считываем 1й элемент как текст.
    # Делаем срез и избавляемся от знака ₽ в начале строки,
    # конвертируем строку в число типа float
    ####price = float(convert[0].text[1:])
    price = convert[0].text
    #print("Цена акции SBER: ", price)
    return price
    #time.sleep(sleep)
    #test_SBER()  # вызываем эту же функцию снова
k = 0
"""if __name__ == '__main__':
    ticker_GAZP = {}
    ticker_SBER = {}
    while(True):
        time.sleep(sleep)

        #print("Цена акции Газпром: ", update_ticker_GAZP())
        #print("Цена акции SBER: ", update_ticker_SBER())
        #update_ticker_GAZP()
        print(datetime.datetime.today())
        ticker_GAZP [datetime.datetime.today()] = update_ticker_GAZP()
        ticker_SBER [datetime.datetime.today()] = update_ticker_SBER()
        #ticker ['SBER'] = update_ticker_SBER()



        d2 = {"id": 1948, "name": "Washer", "size": 3}
        with open('out.txt', 'w') as out:
            for key, val in d2.items():
                out.write('{}:{}\n'.format(key, val))
        with open('api.json','w') as f:
            f.write(ticker_GAZP)
            f.write(ticker_SBER)
"""