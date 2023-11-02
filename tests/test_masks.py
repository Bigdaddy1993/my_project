from src.masks import number_of_account, number_of_card


def test_number_of_card() -> None:
    assert number_of_card("7000792289606361") == "7000 79** **** 6361"


def test_number_of_account() -> None:
    assert number_of_account("73654108430135874305") == "**4305"
