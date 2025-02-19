import pytest
from prime import is_prime


def test_prime():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(5) is True
    assert is_prime(29) is True
    assert is_prime(30) is False
    assert is_prime(1) is False
    assert is_prime(0) is False
    assert is_prime(-9) is False


if __name__ == "__main__":
    pytest.main()
