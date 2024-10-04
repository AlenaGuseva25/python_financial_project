import pytest
from src.decorators import log


def test_log_decorator_no_filename(capsys):
    @log()
    def add(a, b):
        return a + b

    result = add(2, 3)
    assert result == 5

    captured = capsys.readouterr()
    assert captured.out.startswith("add started with inputs: (2, 3), {}\n".format({}))
    assert "add ok, result: 5\n" in captured.out


def test_log_decorator_with_filename(tmp_path):
    filename = tmp_path / "log.txt"

    @log(filename=str(filename))
    def add(a, b):
        return a + b

    result = add(2, 3)
    assert result == 5

    with open(filename, "r") as file:
        log_output = file.read()
    assert log_output.startswith("add started with inputs: (2, 3), {}\n".format({}))
    assert "add ok, result: 5\n" in log_output


def test_log_decorator_with_exception(capsys):
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(2, 0)

    captured = capsys.readouterr()
    assert captured.out.startswith("divide started with inputs: (2, 0), {}\n".format({}))
    assert "divide error: division by zero\n" in captured.out


def test_log_decorator_with_filename_and_exception(tmp_path):
    filename = tmp_path / "log.txt"

    @log(filename=str(filename))
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(2, 0)

    with open(filename, "r") as file:
        log_output = file.read()
    assert log_output.startswith("divide started with inputs: (2, 0), {}\n".format({}))
    assert "divide error: division by zero\n" in log_output
