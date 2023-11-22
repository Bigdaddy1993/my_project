import json
from typing import Any

from src.log import logger


def get_json(path: str) -> Any:
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
    logger.info(f'вернулся список словарей с данными о финансовых транзакциях {operations}')
    return operations


def transactions(operation: dict) -> float | str:
    """
    принимает на вход одну транзакцию
    :param operation: dict
    :return: возвращает сумму транзакции в рублях
    """
    if operation['operationAmount']['currency']['code'] == 'RUB':
        logger.info(f'вернул сумму транзакции в рублях {operation['operationAmount']['amount']}')
        return float(operation['operationAmount']['amount'])
    else:
        raise ValueError("Транзация выполнена не в рублях. Укажите транзакцию в рублях")
