from pathlib import Path

ROOT_PATH = Path(__file__).parent
DATA_PATH = ROOT_PATH.joinpath(ROOT_PATH, 'data')
OPERATIONS_PATH = DATA_PATH.joinpath(DATA_PATH, 'operations.json')
TEST_OPERATIONS_PATH = DATA_PATH.joinpath(DATA_PATH, 'test_operations.json')
TEST_OPERATIONS_PATH_FILE = DATA_PATH.joinpath(DATA_PATH, 'operationzzz.json')
TEST_OPERATIONS_EMPTY = DATA_PATH.joinpath(DATA_PATH, 'test_operations_empty.json')
TRANSACTIONS = DATA_PATH.joinpath(DATA_PATH, 'transactions.csv')
TRANSACTIONS_EXCEL = DATA_PATH.joinpath(DATA_PATH, 'transactions_excel.xlsx')
