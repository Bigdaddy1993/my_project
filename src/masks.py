def number_of_card(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX
    :return:
    """

    mask_number = card_number[:6] + (len(card_number[6:-4]) * "*") + card_number[-4:]
    four_numbers, four_numbers_size = len(mask_number), len(mask_number) // 4
    return " ".join([mask_number[num: num + four_numbers_size] for num in range(0, four_numbers, four_numbers_size)])


def number_of_account(account_number: str) -> str:
    """
    Функция принимает на вход номер счёта и возвращает его маску. Номер счёта замаскирован и отображается в формате
    **XXXX
    :return:
    """

    mask_account_number = account_number[:6] + (len(account_number[10:-4]) * "*") + account_number[-4:]
    four_numbers, four_numbers_size = len(mask_account_number), len(mask_account_number)
    return " ".join(
        [mask_account_number[num: num + four_numbers] for num in range(10, four_numbers, four_numbers_size)]
    )


# print(number_of_card("7000792289606361"))
#
# print(number_of_account("73654108430135874305"))
