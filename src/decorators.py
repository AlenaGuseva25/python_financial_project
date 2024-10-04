from functools import wraps


def log(filename=None):
    """Автоматически логирует начало и конец функции, ее результаты и возникшие ошибки"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            log_message = f"{func.__name__} started with inputs: {args}, {kwargs}\n"
            if not filename:
                print(log_message, end="")
            else:
                with open(filename, "a") as file:
                    file.write(log_message)

            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok, result: {result}\n "
                if not filename:
                    print(log_message, end="")
                else:
                    with open(filename, "a") as file:
                        file.write(log_message)
                return result
            except Exception as e:
                log_message = f"{func.__name__} error: {e}\n"
                if not filename:
                    print(log_message, end="")
                else:
                    with open(filename, "a") as file:
                        file.write(log_message)
                raise

        return wrapper

    return decorator


@log(filename="log.txt")
def add(a, b):
    return a + b
