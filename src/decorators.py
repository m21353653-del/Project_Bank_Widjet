from functools import wraps
from typing import Callable
from pathlib import Path


def log(filename: str = "config.ini") -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            decorator_result = ""
            try:
                result = func(*args, **kwargs)
                decorator_result = f"{func.__name__}: {result}"
            except Exception as e:
                decorator_result = f"{func.__name__}: {e}. Входные параметры: {args}"

            if filename != "config.ini":
                # Получаем корень проекта (на уровень выше src)
                project_root = Path(__file__).parent.parent
                # Формируем путь: корень проекта → папка logs → файл
                log_file = project_root / "logs" / filename

                with open(log_file, "w", encoding='utf-8') as f:
                    f.write(decorator_result)

                return result

            # Если условие не выполняется, тогда выводим в консоль
            print(decorator_result)
            return result

        return wrapper
    return decorator
