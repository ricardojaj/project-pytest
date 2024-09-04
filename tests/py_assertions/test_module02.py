import pytest


def test_case01():
    with pytest.raises(Exception):
        assert (1/0)

def test_case02():
    with pytest.raises(Exception):
        assert (1, 2, 3) == (1, 2, 4)


