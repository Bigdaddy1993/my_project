import pandas as pd
import csv

from settings import TRANSACTIONS, TRANSACTIONS_EXCEL


def read_data():
    """
    Открывает файл и читает его , формат csv
    :return: список транзакций из файла
    """
    transactions = []
    with open(TRANSACTIONS, encoding='utf-8', newline='') as file:
        data_open = csv.DictReader(file, delimiter=';')
        for raw in data_open:
            transactions.append(raw)
    return transactions


def read_xlsx():
    """
    преобразовывает данные из файла xlsx в список транзакций
    :return: список транзакций
    """
    data = pd.read_excel(TRANSACTIONS_EXCEL)
    transactions = data.to_dict('records')
    return transactions
