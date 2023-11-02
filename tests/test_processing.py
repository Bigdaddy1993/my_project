import pytest

from src.processing import sort_date, sort_dict


@pytest.fixture()
def data() -> list[dict[str, str]]:
    return [
        {"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": "939719570", "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "inner_data, expected",
    [
        (
            "EXECUTED",
            [
                {"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": "939719570", "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
    ],
)
def test_sort_dict(data: list[dict[str, str]], inner_data: str, expected: list[dict[str, str]]) -> None:
    assert sort_dict(data, inner_data) == expected


@pytest.fixture()
def stock_data():
    return [
        {"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": "939719570", "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.mark.parametrize(
    "inner_data, expected",
    [
        (
            True,
            [
                {"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": "939719570", "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": "939719570", "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_date(stock_data: list[dict[str, str]], inner_data: bool, expected: list[dict[str, str]]) -> None:
    assert sort_date(stock_data, inner_data) == expected
