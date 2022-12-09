def func(x: int = 0):
    return x + 1


def test_answer():
    assert(func(3)) == 4
