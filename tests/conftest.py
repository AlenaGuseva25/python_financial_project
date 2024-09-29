import pytest


@pytest.fixture
def dat() -> str:
    return "12345678912345678900"

@pytest.fixture
def expec() -> str:
    return "**8900"