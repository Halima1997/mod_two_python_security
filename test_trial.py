import unittest
from trial import username, status_code, user_id


def test_check_status_code_equals_200():
    expected = 200
    actual = status_code('32801417')
    assert expected == actual


def test_username():
    expected = ['halimaabdi', 'halima97']
    actual = username('32801417')
    assert expected == actual


def test_user_id():
    expected = 10436975, 10141796
    actual = user_id('32801417')
    assert expected == actual


if __name__ == '__main__':
    unittest.main()
