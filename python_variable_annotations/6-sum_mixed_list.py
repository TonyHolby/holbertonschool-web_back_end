#!/usr/bin/env python3
"""
    Defines a method named sum_mixed_list that takes a list mxd_lst of
    integers and floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Returns the sum of the lists as a float. """
    return sum(mxd_lst)
