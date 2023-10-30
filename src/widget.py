from src.masks import number_of_card, number_of_account


def type_of_info(masking: str) -> str:
    """Принимает на вход строку с информацией: тип карты/счета и номер карты/счета
        Возвращает тип карты/счета и замаскированный номер карты/счета."""
    list_mask = masking.split()
    joined = ' '.join(list_mask[:-1])

    if 'счет' == list_mask[0].lower():
        return f'{joined} {number_of_account(list_mask[-1])}'
    return f'{joined} {number_of_card(list_mask[-1])}'


def datetime_of_operation(date_and_time: str) -> str:
    """Принимает на вход строку, вида "2018-07-11T02:26:18.671407"
    возвращает строку с датой в виде "11.07.2018"""
    date = date_and_time.split("T")
    return ".".join(reversed(date[0].split("-")))
