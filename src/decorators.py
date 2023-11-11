import datetime
from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                message = f'{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, {func.__name__} ok\n'
            except Exception as ex:
                result = None
                message = f'{datetime.datetime.now()} {func.__name__} error {str(ex)}.'
            if filename:
                with open(filename, 'a') as file:
                    file.write(message)
            else:
                print(message)
            return result

        return inner

    return wrapper


@log()
def my_function(x, y):
    return x + y


my_function(3, 2)
