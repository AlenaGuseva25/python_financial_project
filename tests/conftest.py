import pytest


@pytest.fixture
def dat() -> str:
    return "12345678912345678900"

@pytest.fixture
def expec() -> str:
    return "**8900"

@pytest.fixture
def date() -> str:
    return "2024-03-11T02:26:18.671407"

@pytest.fixture
def total_date() -> str:
    return "11.03.2024"