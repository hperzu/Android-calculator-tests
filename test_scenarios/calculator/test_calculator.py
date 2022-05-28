import pytest


def test_calculator_is_launched(calculator_mian_page):
    assert calculator_mian_page.is_launched()


@pytest.mark.parametrize("a,b,result", [(1, 2, 3), (2, 4, 6), (5, 6, 11)])
def test_check_result_of_two_numbers_added(calculator_mian_page, a, b, result):
    assert result == int(calculator_mian_page.add_two_numbers(a, b))


@pytest.mark.parametrize("a,b,result", [(1, 2, 2), (2, 4, 8), (5, 6, 30)])
def test_check_results_of_two_numbers_multiplied(calculator_mian_page, a, b, result):
    assert result == int(calculator_mian_page.multiply_two_numbers(a, b))
