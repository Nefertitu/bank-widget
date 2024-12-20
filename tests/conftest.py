from typing import Tuple

import pytest


@pytest.fixture
def card_number_for_test() -> str:
    return "7000 79** **** 6361"


@pytest.fixture
def card_error_number_for_test() -> tuple[str, str]:
    return "1234567891234678", "123456789123456"


@pytest.fixture
def account_number_for_test() -> str:
    return "73654108430135874305"


@pytest.fixture
def account_error_number_for_test() -> tuple[str, str]:
    return "73654108430135874305", "73654108430133051111"
