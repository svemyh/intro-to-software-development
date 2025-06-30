import numpy as np

def find_average(list_of_numbers: list[int]) -> float:
    avg = np.average(list_of_numbers)
    return float(avg)