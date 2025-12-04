from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1) == 2

    assert arrs.get([1, 2, 3], 3, "default") == "default"

    assert arrs.get([1, 2, 3], -1, "default") == "default"

    assert arrs.get([], 0, "default") == "default"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]

    assert arrs.my_slice([]) == []

    assert arrs.my_slice([], 0, 5) == []

    assert arrs.my_slice([1, 2, 3]) == [1, 2, 3]

    assert arrs.my_slice([1, 2, 3, 4, 5], None, 3) == [1, 2, 3]

    assert arrs.my_slice([1, 2, 3, 4, 5], None, None) == [1, 2, 3, 4, 5]

    assert arrs.my_slice([1, 2, 3, 4, 5], 2, None) == [3, 4, 5]

    assert arrs.my_slice([1, 2, 3], 0, 10) == [1, 2, 3]

    assert arrs.my_slice([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]

    assert arrs.my_slice([1, 2, 3, 4, 5], -3, -1) == [3, 4]

    assert arrs.my_slice([1, 2, 3, 4, 5], 0, 0) == []