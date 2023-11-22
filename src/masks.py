from src.log import logger


def number_of_card(card_number: str) -> str:
    """
    Функция принимает на вход номер карты и возвращает ее маску. Номер карты замаскирован и отображается в формате
    XXXX XX** **** XXXX
    :return:
    """

    mask_number = card_number[:6] + (len(card_number[6:-4]) * "*") + card_number[-4:]
    four_numbers_size = 4
    mask_number_card = " ".join(
        [mask_number[num : num + four_numbers_size] for num in range(0, len(mask_number), four_numbers_size)]
    )
    logger.info(f"Номер карты замаскирован {mask_number_card}")
    return mask_number_card


def number_of_account(account_number: str) -> str:
    """
    Функция принимает на вход номер счёта и возвращает его маску. Номер счёта замаскирован и отображается в формате
    **XXXX
    :return:
    """

    mask_number = (len(account_number[:-4]) * "*") + account_number[-4:]
    sliced = mask_number[-6:]
    logger.info(f"Номер счёта замаскирован {sliced}")
    return sliced
