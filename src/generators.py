from typing import Any, Generator

from random import randint

transactions1 = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transactions: list[dict], currency: str) -> Generator:
    """
    принимает список словарей
    :param transactions: список словарей
    :param currency: валюта, например 'USD'
    :return: возвращает итератор который выдает по очереди операции
    в которых указана заданная валюта
    """
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency.upper():
            yield transaction


usd_transactions = filter_by_currency(transactions1, 'USD')
for _ in range(3):
    print(next(usd_transactions)['id'])


def transaction_descriptions(transactions: list[dict]) -> Generator:
    """
    принимает список словарей.
    :param transactions: список словарей
    :return: возвращает описание каждой операции по очереди
    """
    for transaction in transactions:
        yield transaction['description']


description_of_operations = transaction_descriptions(transactions1)

for _ in range(5):
    print(next(description_of_operations))


def card_number_generator(start: int, stop: int) -> Generator:
    """
    генерирует номера карт в формате "XXXX XXXX XXXX XXXX", где X — цифра
    :param start: диапозон начала генерации
    :param stop: диапозон конца генерации
    :return: возращает номер карты в виде XXXX XXXX XXXX XXXX
    """
    generator = 16 - len(str(stop))
    for number in range(start, stop + 1):
        number_generator = (generator * '0') + str(number)
        yield f'{number_generator[0:4]} {number_generator[4:8]} {number_generator[8:12]} {number_generator[12:]}'


for card_number in card_number_generator(1, 5):
    print(card_number)
