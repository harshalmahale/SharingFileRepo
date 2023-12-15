import pytest
from my_math_lib import add
input_list = [
    (1, 2, 3),
    (4, 5, 9),
    ("Thank", " you", "Thank you"),
    (1.5, 3.5, 5)]

pytest.param(5, 5, 5, marks=[pytest.mark.xfail])
pytest.param(5, 5, 5, marks=[pytest.mark.xfail, pytest.mark.skip])
pytest.param(5, 5, 10, marks=[pytest.mark.xfail])

@pytest.mark.parametrize('p1, p2, r', input_list)
def test_add(p1, p2, r):
    assert add(p1, p2) == r

