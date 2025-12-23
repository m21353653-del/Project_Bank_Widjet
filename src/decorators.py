from functools import wraps
from pathlib import Path
from typing import Any, Callable


def log(filename: str = "config.ini") -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            decorator_result = ""
            # Получаем корень проекта (на уровень выше src)
            project_root = Path(__file__).parent.parent
            # Формируем путь: корень проекта → папка logs → файл
            log_file = project_root / "logs" / filename

            if filename != "config.ini":
                with open(log_file, "a", encoding="utf-8") as f:
                    f.write(f"{func.__name__}: Запуск, параметры: {args}\n")
            else:
                print(f"{func.__name__}: Запуск, параметры: {args}")

            try:
                result = func(*args, **kwargs)
                decorator_result = f"{func.__name__}: результат - {result}"
            except Exception as e:
                decorator_result = f"{func.__name__}: {e}. Входные параметры: {args}"

            if filename != "config.ini":
                with open(log_file, "a", encoding="utf-8") as f:
                    f.write(f"{decorator_result}\n")

                return None

            # Если условие не выполняется, тогда выводим в консоль
            print(decorator_result)
            return None

        return wrapper

    return decorator


@log()
def my_function(text):
    return text

my_function()