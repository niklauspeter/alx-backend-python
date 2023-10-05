#!/usr/bin/env python3
"""type-annotated function make_multiplier that
takes a float multiplier as argument and
returns a function that multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns function that multiplieas float by multiplier
    Args:
        multiplier (float): The multiplier
    Returns:
        A function that multiplies a float by multiplier
    """

    def multiplier_func(number: float) -> float:
        """Multiplies a float by multiplier"""
        return multiplier * number

    return multiplier_func
