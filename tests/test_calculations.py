from geo_calculator.calculations import find_average, gardners_equation, inverse_gardners_equation

import pytest

def test_length_of_string() -> None:
    test_string = "python"
    assert len(test_string) == 6

def test_find_average_of_list_of_numbers() -> None:
    test_list = [1, 2, 3, 4, 5, 6]
    assert find_average(test_list) == 3.5

def test_gardners_equation():
    velocity = 2000  # m/s
    expected_density = 2.0730949  # g/cm3

    # By default, approx considers numbers within a relative tolerance of 1e-6
    assert gardners_equation(velocity) == pytest.approx(expected_density)

def test_inverse_gardners_equation() -> None:
    density = 2.0730949  # g/cm3
    expected_velocity = 2000  # m/s

    assert inverse_gardners_equation(density) == pytest.approx(expected_velocity)

    assert inverse_gardners_equation(
        gardners_equation(expected_velocity)
    ) == pytest.approx(expected_velocity)

    assert gardners_equation(inverse_gardners_equation(density)) == pytest.approx(
        density
    )