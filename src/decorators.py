from functools import wraps
from typing import Any, Callable, Optional

from datetime import datetime


def log(filename: Optional[str] = None) -> Callable:
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            try:
                result = func(*args, **kwargs)
                message = f'{time} {func.__name__} ok\n'
            except Exception as ex:
                result = None
                message = f'{time} {func.__name__} error {str(ex)} {args} {kwargs}'
            if filename:
                with open(filename, 'a') as file:
                    file.write(message)
            else:
                print(message)
            return result

        return inner

    return wrapper
