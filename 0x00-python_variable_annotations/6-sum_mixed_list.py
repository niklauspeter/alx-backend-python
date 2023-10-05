#!/usr/bin/env python3
"""
functions takes in a list of numbers of
mixed types and returns the sum as float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes list of floats and integers and returns
    sum of all numbers in the list as float"""
    return sum(mxd_lst)
