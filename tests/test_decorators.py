import os.path
from datetime import datetime

import pytest

from src.decorators import log


@pytest.mark.parametrize('arg_1, arg_2, expected_result', [(1, 0, ' foo error division by zero (1, 0) {}'),
                                                           (1, 2, ' foo ok')])
def test_log_decorator(arg_1, arg_2, expected_result):
    filename = 'my_test.txt'
    if os.path.exists(filename):
        os.remove(filename)

    @log(filename)
    def foo(x: int, y: int) -> float:
        return x / y

    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    foo(arg_1, arg_2)

    with open(filename) as f:
        log_message = f.read().strip()

    assert log_message == time + expected_result


@pytest.mark.parametrize('arg_1, arg_2, expected_result', [(1, 0, ' foo error division by zero (1, 0) {}'),
                                                           (1, 2, ' foo ok')])
def test_console(capsys, arg_1, arg_2, expected_result):
    @log()
    def foo(x: int, y: int) -> float:
        return x / y

    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    foo(arg_1, arg_2)

    expected_log = time + expected_result

    log_mess = capsys.readouterr()
    assert log_mess.out.strip() == expected_log
