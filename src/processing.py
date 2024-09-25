def filter_by_state(data: list[dict[str, str]], state: str = "EXECUTED") -> list[dict[str, str]]:
    """Функция возвращает список словарей по ключу state с указанным значением"""
    return [d for d in data if d.get("state") == state]


def sort_by_date():
    """Функция сортировки списка словарей по дате"""
    pass