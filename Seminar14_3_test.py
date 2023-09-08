# pytest

from Seminar14_3_main import sum2


def test_sum2():
    assert sum2(13, 8) == 21
    assert sum2(15, 8) == 23
    assert sum2(17, 9) == 27
