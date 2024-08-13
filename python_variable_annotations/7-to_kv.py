#!/usr/bin/env python3
"""
    Defines a method named sum_mixed_list that takes a string k
    and an int or float v as arguments and returns a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple. """
    return k, float(v ** 2)
