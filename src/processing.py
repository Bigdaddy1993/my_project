def sort_dict(list_of_dict: list[dict], get_argument="EXECUTED") -> list[dict]:
    """принимает на вход список словарей и значение
    для ключа state (опциональный параметр со значением по умолчанию  EXECUTED)
    и возвращает новый список, содержащий только те словари, у которых ключ
    state
    содержит переданное в функцию значение"""
    return [i for i in list_of_dict if i["state"] == get_argument.upper()]


list_of_operation = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(sort_dict(list_of_operation))

list_of_date = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def sort_date(list_of_dict: list[dict]) -> list[dict]:
    """принимает на вход список словарей и возвращает новый список
    в котором исходные словари отсортированы по убыванию даты"""
    sorted_date = sorted(list_of_dict, key=lambda date: date["date"], reverse=True)
    return sorted_date


print(sort_date(list_of_date))
