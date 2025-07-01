import numpy as np


def find_average(list_of_numbers: list[int]) -> float:
    """Calculate the average of some numbers
    Args:
        numbers: A sequence of numbers
    Returns:
        The average value of the numbers
    """
    avg = np.average(list_of_numbers)
    return float(avg)


GARDNERS_ALPHA = 0.31
GARDNERS_BETA = 0.25


def gardners_equation(velocity: float) -> float:
    """Calculate density from velocity using Gardner's equation"""
    if velocity < 0:
        raise ValueError("Velocity cannot be negative.")
    density = GARDNERS_ALPHA * velocity**GARDNERS_BETA
    return density


def inverse_gardners_equation(density: float) -> float:
    """Calculate velocity from density using Gardner's equation"""
    if density < 0:
        raise ValueError("Density cannot be negative.")
    velocity = (density / GARDNERS_ALPHA) ** (1 / GARDNERS_BETA)
    return velocity
