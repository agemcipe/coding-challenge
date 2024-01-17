import pytest

from collections import OrderedDict

from coding_challenge.main import fold

@pytest.mark.parametrize(
    "ls, start, fn, expected", [
        ([], 0, lambda x,y: x+y, 0),
    ]
)
def test_empty_sequence(ls, start, fn, expected):
    assert fold(ls, start, fn) == expected


@pytest.mark.parametrize(
    "ls, start, fn, expected", [
        (1, 0, lambda x,y: x+y, 0),
    ]
)
def test_non_iterable_sequence(ls, start, fn, expected):
    with pytest.raises(ValueError):
        fold(ls, start, fn) == expected


@pytest.mark.parametrize(
    "ls, start, fn, expected", [
        ([1, 2, 3], 0, lambda x, y: x + y, 6),
        ([1, 2, 3], 1, lambda x, y: x + y, 7 )
    ]
)
def test_fold_sum(ls, start, fn, expected):
    assert fold(ls, start, fn) == expected



@pytest.mark.parametrize(
    "ls, start, fn, expected", [
        ([1, 2, 3], 1, lambda x, y: x * y, 6),
    ]
)
def test_fold_multiplication(ls, start, fn, expected):
    assert fold(ls, start, fn) == expected


@pytest.mark.parametrize(
    "ls, start, fn, expected", [
        ("abcd", "", lambda x, y: x + y, "abcd"),
    ]
)
def test_fold_string_concatenation(ls, start, fn, expected):
    assert fold(ls, start, fn) == expected

@pytest.mark.parametrize(
    "ls, start, fn, expected", [
       (OrderedDict({0: 0, 1:1, 2:3}), 0, lambda x,y: x+y, 3)  # this sums over the keys not the values of the OrderedDict
    ]
)
def test_fold_non_list(ls, start, fn, expected):
    assert fold(ls, start, fn) == expected