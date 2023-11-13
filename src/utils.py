import json

from src.settings import OPERATIONS_PATH


def get_json(path):
    try:
        with open(path, encoding='utf8') as file:
            operations = json.load(file)
    except FileNotFoundError:
        operations = []
    except json.JSONDecodeError:
        operations = []
    return operations


def transactions(operation):
    if operation['operationAmount']['currency']['code'] == 'RUB':
        return operation['operationAmount']['amount']
    else:
        raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")


print(transactions({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
        "amount": "8221.37",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
}))
