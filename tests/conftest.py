import pytest


@pytest.fixture
def card_number_for_test() -> str:
    return "7000 79** **** 6361"


@pytest.fixture
def account_number_for_test() -> str:
    return "73654108430135874305"
