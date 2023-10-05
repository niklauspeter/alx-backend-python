#!/usr/bin/env python3
"""function takes in string and int/float as arguments,
returns set containing string and square of int or float
basically function converts the Python variable to a KV pair."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Converts a Python variable to a KV pair."""
    return k, v ** 2
