#!/usr/bin/env python3
"""function returns the sum of a list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """adds up the float elements in list
    Args:
        input_list (list): the list of floats
    Returns:
        float: sum of the elements in list
    """
    if input_list is None:
        return 0
    else:
        return sum(input_list)
