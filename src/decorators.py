from functools import wraps

def log(filename=None):
    """Автоматически логирует начало и конец функции, ее результаты и возникшие ошибки"""


    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not filename:
                print(f"{func.__name__} started")
                try:
                    func(*args, **kwargs)
                    print(f"{func.__name__} ok")
                    print(f"{func.__name__} finished")
                except Exception as e:
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
            else:
                try:
                    func(*args, **kwargs)
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} ok")
                except Exception as e:
                    with open(filename, "w") as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")
            # return result

        return wrapper

    return decorator

