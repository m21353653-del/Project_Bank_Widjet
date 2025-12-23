from pathlib import Path

import pytest

from src.decorators import log


def test_log_terminal(capsys):
    @log()
    def my_function(x, y):
        return x / y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function: Запуск, параметры: (1, 2)\nmy_function: результат - 0.5\n"

    my_function(5, 0)
    captured = capsys.readouterr()
    assert (
        captured.out
        == "my_function: Запуск, параметры: (5, 0)\nmy_function: division by zero. Входные параметры: (5, 0)\n"
    )


@pytest.mark.parametrize("answer", ["my_function: Запуск, параметры: ('hello!',)\nmy_function: результат - hello!\n"])
def test_log_terminal_2(capsys, answer):
    @log()
    def my_function(text):
        return text

    my_function("hello!")
    captured = capsys.readouterr()
    assert captured.out == answer


def test_log(my_file):
    filename = my_file
    project_root = Path(__file__).parent.parent
    log_file = project_root / "logs" / filename

    @log(filename="test_mylog.txt")
    def my_function(x, y):
        return x / y

    my_function(1, 2)
    my_function(5, 0)

    with open(log_file, "r", encoding="utf-8") as f:
        content = f.read()

    assert "my_function: Запуск, параметры: (1, 2)" in content
    assert "my_function: результат - 0.5" in content

    assert "my_function: Запуск, параметры: (5, 0)" in content
    assert "my_function: division by zero. Входные параметры: (5, 0)" in content
