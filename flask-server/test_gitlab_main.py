import unittest
from gitlab_main import usernames, user_ids


def test_username():
    expected = ['halimaabdi', 'halima97']
    actual = usernames(32801417)
    assert expected == actual


def test_user_id():
    expected = [10436975, 10141796]
    actual = user_ids(32801417)
    assert expected == actual


if __name__ == '__main__':
    unittest.main()
