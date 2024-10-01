from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(data: list[dict], state: str, tota: list[dict]) -> None:
    assert filter_by_state(data, state) == tota


def test_filter_by_data_2(data: list[dict], state_1: str, tota_1: list[dict]) -> None:
    assert filter_by_state(data, state_1) == tota_1


def test_sort_by_date(date_list: list[dict], direction: bool, conclusion: list[dict]) -> None:
    assert sort_by_date(date_list, direction) == conclusion


def test_sort_by_date_2(date_list: list[dict], direction_2: bool, conclusion_2: list[dict]) -> None:
    assert sort_by_date(date_list, direction_2) == conclusion_2
