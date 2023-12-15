# # # # def test_recursion_depth():
# # # #     with pytest.raises(RuntimeError) as exception_info:
# # # #         f()
# # # #     assert "maximum recursion" in str(exception_info.value)
# # #
# # # def test_set_comparison():
# # #     set1 = set("1308")
# # #     set2 = set("8031")
# # #     # set2 = set("8035")
# # #     assert set1 == set2
abc = 'Hi'

import pytest


def test_passsing():
    assert (1, 2, 3) == (1, 2, 3)


@pytest.mark.skip(reason="welcome message")
def test_passing1():
    assert (2, 3, 1) == (2, 3, 1)


@pytest.mark.skipif('abc == "Hi"', reason="welcome message")
def test_passing2():
    assert (2, 3, 1) == (2, 3, 1)
#
# abc = "Hi"
# def test_passing():
#     assert (1, 2, 3) == (1, 2, 3)
# @pytest.mark.skip()
# def test_passing1():
#     assert (2, 3, 1) == (2, 3, 1)
# @pytest.mark.skipif('abc == "Hi"')
# def test_passing2():
#     assert (2, 3, 1) == (2, 3, 1)
# @pytest.mark.skipif('abc == "Hi"', reason="Required Welcome message not set")
# def test_passing3():
#     assert (2, 3, 1) == (2, 3, 1)
