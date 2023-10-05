from typing import Tuple, List

"""
Function returns a list of integers
multiplied by specified factor
passed as argument.
"""

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Returns list of integers multiplied by particular factor.
    Args:
        lst: A tuple of integers.
        factor: An integer.
    Returns:
        A list of integers.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
