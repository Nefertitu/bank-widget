from decorators import log, my_function


@log(filename=None)
def test_log_is_None_positive_console(capsys):
    my_function(1, 5)
    captured = capsys.readouterr()
    assert captured.out == "'my_function' with args: (1, 5) and kwargs: {}.\nResult = 0.2.\n"


@log(filename=None)
def test_log_is_None_negative_zero_console(capsys):
    my_function(1, 0)
    captured = capsys.readouterr()
    assert captured.out == "None\n"


@log(filename=None)
def test_log_not_is_None_positive_first_zero_console(capsys):
    my_function(0, 5)
    captured = capsys.readouterr()
    assert captured.out == "'my_function' with args: (0, 5) and kwargs: {}.\nResult = 0.0.\n"


@log(filename=None)
def test_log_is_None_negative_type_error_console(capsys):
    my_function(1, "1")
    captured = capsys.readouterr()
    assert captured.out == "None\n"


def test_log_is_None_negative_zero():
    @log(filename=None)
    def log_is_None_negative_zero():
        result = my_function(5, 0)
        assert result == "'my_functions' error: ZeroDivisionError: division by zero. Inputs: (5, 0), {}"


def test_log_is_None_positive():
    @log(filename=None)
    def log_is_None_positive():
        result = my_function(1, 5)
        assert (
            result == """'my_functions' with args: (1, 5) and kwargs: {}.
            \nResult = 0.2. \nTime execution: 0.000001 \n0.2"""
        )


@log(filename=None)
def test_log_is_None_out_err(capsys):
    my_function(1, "5")
    out, err = capsys.readouterr()
    assert out == "None\n"
    assert err == ""


@log(filename="mylog.txt")
def test_log_output_to_file():
    result = my_function(8.8, 4)
    with open("mylog.txt", "r") as file:
        content = file.read()

    assert result == content
