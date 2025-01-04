import datetime
import logging
from functools import wraps
from time import time
from typing import Any, Callable


def log(filename: None | str = None) -> Any:
    def decorator(function: Any) -> Any | None:
        @wraps(function)
        def wrapper(*args: int | float, **kwargs: Any) -> Any:
            try:
                result = function(*args, **kwargs)

            except Exception as exc_info:
                if filename is not None:
                    logging.basicConfig(level=logging.ERROR, filename="mylog.txt", filemode="w", format="%(message)s, \n%(asctime)s")
                    logging.error(f"'{function.__name__}' error: {type(exc_info).__name__}: {str(exc_info)}. "
                        f"Inputs: {args}, {kwargs}")
                if filename is None:
                    print(logging.basicConfig(level=logging.ERROR, format="%(message)s"))
                    logging.error(f"'{function.__name__}' error: {type(exc_info).__name__}: {str(exc_info)}. "
                                  f"Inputs: {args}, {kwargs}")

            else:
                if filename is None:
                    function_call_time = datetime.datetime.now()
                    start_time = time()
                    result = function(*args, **kwargs)
                    end_time = time()
                    print(f"'{function.__name__}' with args: {args} and kwargs: {kwargs}." f"\nResult = {result}.")

                    return result

                if filename is not None:
                    with open(filename, "w") as file:
                        function_call_time = datetime.datetime.now()
                        start_time = time()
                        result = function(*args, **kwargs)
                        end_time = time()
                        file.write(
                            f"'{function.__name__}' with args: {args} and kwargs: {kwargs}. \nResult = {result}."
                            f"\nFunction call time: {function_call_time}."
                            f"\nTime execution: {end_time - start_time:.7f}"
                        )
                        return "my_function ok"

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int | float, y: int | float) -> Any:
    """
    Выполняет сложение полученных значений
    :param x:
    :param y:
    :return:
    """
    return x / y


print(my_function(8.8, 4))
