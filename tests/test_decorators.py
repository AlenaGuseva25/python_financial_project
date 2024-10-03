from src.decorators import log


@log()
def my_function(x, y):
    return x / y


def test_log_print(capsys):
    my_function(10, 5)
    captured = capsys.readouterr()
    expected_output = "my_function started\n" "my_function ok\n" "my_function finished\n"
    assert captured.out == expected_output


def test_log_print_try(capsys):
    my_function(10, 0)
    captured = capsys.readouterr()
    expected_output = "my_function started\n" "my_function error: division by zero. Inputs: (10, 0), {}\n"
    assert captured.out == expected_output


def test_log_print_fail(tmp_path):
    log_file = tmp_path / "test_output.txt"

    @log(log_file)
    def my_function(x, y):
        return x / y

    my_function(10, 5)
    with open(log_file, "r") as f:
        content = f.read()
    assert content == "my_function ok"


def test_log_print_fail_try(tmp_path):
    log_file = tmp_path / "test_output.txt"

    @log(log_file)
    def my_function(x, y):
        return x / y

    my_function(10, 0)
    with open(log_file, "r") as f:
        content = f.read()
    assert content == "my_function error: division by zero. Inputs: (10, 0), {}"
