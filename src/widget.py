from masks import number_of_card, number_of_account


def type_of_cards(type_and_number: str , account_and_number) -> str:
    """Принимает на вход строку информацией тип карты/счета и номер карты/счета
    Возвращает тип карты/счета и замаскированный номер карты/счета."""
    split_list = type_and_number.split()
    split_account = account_and_number.split()
    only_account = number_of_account(split_account[-1])
    only_number_account = split_account[:1]
    join_oneline = "".join(only_number_account)
    if len(split_list) == 3:
        only_number = number_of_card(split_list[-1])
        only_type = split_list[:2]
        join_only_type = " ".join(only_type)
        return f"{join_only_type} {only_number} \n{join_oneline} {only_account}"
    elif len(split_list) == 2:
        only_number = number_of_card(split_list[-1])
        only_type = split_list[:1]
        join_only_type = " ".join(only_type)
        return f"{join_only_type} {only_number} \n{join_oneline} {only_account}"
    else:
        return "не знаю такой номер карты/счета"


print(type_of_cards("Visa 8990922113665229", "Счет 64686473678894779589"))


def datetime_of_operation(date_and_time: str) -> str:
    """Принимает на вход строку, вида "2018-07-11T02:26:18.671407"
    возвращает строку с датой в виде "11.07.2018"""
    date = date_and_time.split("T")
    return ".".join(reversed(date[0].split("-")))


print(datetime_of_operation("2018-07-11T02:26:18.671407"))
