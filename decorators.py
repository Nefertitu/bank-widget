import datetime
import logging
from functools import wraps
from time import time
from typing import Any


def log(filename: None | str = None) -> Any:
    def decorator(function: Any) -> Any | None:
        @wraps(function)
        def wrapper(*args: int | float, **kwargs: Any) -> Any:
            try:
                function(*args, **kwargs)

            except Exception as exc_info:
                if filename:
                    logging.basicConfig(
                        level=logging.ERROR, filename="mylog.txt", filemode="w", format="%(message)s, \n%(asctime)s"
                    )

                    logging.error(
                        f"{function.__name__} error: {type(exc_info).__name__}: {str(exc_info)}. "
                        f"Inputs: {args}, {kwargs}"
                    )
                if filename is None:
                    logging.basicConfig(level=logging.ERROR, format="%(message)s")
                    return (
                        f"{function.__name__} error: {type(exc_info).__name__}: {str(exc_info)}. "
                        f"Inputs: {args}, {kwargs}"
                    )

            else:
                if filename is None:
                    result = function(*args, **kwargs)
                    return f"{function.__name__} with args: {args} and kwargs: {kwargs}. Result = {result}."

                if filename:
                    with open(filename, "w") as file:
                        function_call_time = datetime.datetime.now()
                        start_time = time()
                        result = function(*args, **kwargs)
                        end_time = time()
                        file.write(
                            f"{function.__name__} with args: {args} and kwargs: {kwargs}. \nResult = {result}."
                            f"\nFunction call time: {function_call_time}."
                            f"\nTime execution: {end_time - start_time:.7f}"
                        )
                        return "my_function ok"

        return wrapper

    return decorator


@log(filename="mylog.txt")
def my_function(x: int | float, y: int | float) -> Any:
    """
    Выполняет деление полученных значений
    :param x:
    :param y:
    :return:
    """
    if y == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    if not ((type(x) is int or type(x) is float) and (type(y) is int or type(x) is float)):
        raise TypeError("Value must be an integer or float")

    return x / y


# print(my_function(1, 2))
