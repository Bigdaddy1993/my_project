import unittest.mock
import pandas as pd

from src.read_data import read_data, read_xlsx


def test_read_csv_mock():
    with unittest.mock.patch('src.read_data.csv.DictReader') as mock_reader:
        mock_reader.return_value = [{'id': '1', 'name': 'Roman'}]
        result = read_data()
    assert result == [{'id': '1', 'name': 'Roman'}]


def test_read_xlsx_mock():
    with unittest.mock.patch('src.read_data.pd.read_excel') as mock_reader:
        mock_reader.return_value = pd.DataFrame({'id': [1, 2]})
        result = read_xlsx()
    assert result == [{'id': 1}, {'id': 2}]
