from decorators import my_function


def test_log_is_none_negative_zero_console(capsys):
    print(my_function(1, 0))
    captured = capsys.readouterr()
    assert captured.out == "my_function error: ZeroDivisionError: Cannot divide by zero. Inputs: (1, 0), {}\n"


def test_log_not_is_none_positive_first_zero_console(capsys):
    print(my_function(0, 5))
    captured = capsys.readouterr()
    assert captured.out == "my_function with args: (0, 5) and kwargs: {}. Result = 0.0.\n"


def test_log_is_none_negative_type_error_console(capsys):
    print(my_function(1, "1"))
    captured = capsys.readouterr()
    assert captured.out == "my_function error: TypeError: Value must be an integer or float. Inputs: (1, '1'), {}\n"


def test_log_is_none_positive():
    assert my_function(1, 5) == "my_function with args: (1, 5) and kwargs: {}. Result = 0.2."
