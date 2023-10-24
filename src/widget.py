from masks import number_of_card


def type_of_cards(type_and_number: str | list[str]) -> str:
    """Принимает на вход строку информацией тип карты и номер карты
       Возвращает тип карты и замаскированный номер карты."""
    split_list = type_and_number.split()
    only_number = number_of_card(split_list[-1])
    only_type = split_list[:1]
    join_only_type = ''.join(only_type)
    return f'{join_only_type} {only_number}'


print(type_of_cards('Maestro 1596837868705199'))
