import json


def get_json(path: str) -> list[dict]:
    """
    принимает на вход путь до JSON-файла
    :param path: path
    :return: возвращает список словарей с данными о финансовых транзакциях
    """
    try:
        with open(path, encoding='utf8') as file:
            operations = json.load(file)
    except FileNotFoundError:
        operations = []
    except json.JSONDecodeError:
        operations = []
    return operations


def transactions(operation: dict) -> float | str:
    """
    принимает на вход одну транзакцию
    :param operation: dict
    :return: возвращает сумму транзакции в рублях
    """
    if operation['operationAmount']['currency']['code'] == 'RUB':
        return float(operation['operationAmount']['amount'])
    else:
        raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")
