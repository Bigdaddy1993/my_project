import re
from collections import Counter


def filter_by_search(transactions: list[dict], search: str) -> list[dict]:
    """

    :param transactions: список словарей с данными о банковских операциях
    :param search: строка поиска
    :return: список словарей, у которых в описании есть данная строка поиска
    """
    result = []
    pattern = re.compile(search, re.IGNORECASE)
    for transaction in transactions:
        description = transaction.get("description", "")
        if re.search(pattern, description):
            result.append(transaction)
    return result


def filter_by_category(transactions: list[dict[str, str]], list_of_category: dict[str, str]) -> Counter:
    """

    :param transactions: список словарей с данными о банковских операциях
    :param list_of_category: словарь категорий операций
    :return: словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории
    """
    counted = Counter(
        transactions.get("category", "") for transaction in transactions if
        transaction.get("category", "") in list_of_category
    )
    return counted
