#!/usr/bin/env python3
"""
    Defines a function named make_multiplier that takes a float multiplier as
    argument and returns a function that multiplies a float by multiplier.
"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Defines a function that multiplies a float by multiplier. """
    def multiplier_function(x: float) -> float:
        """ Returns the value of the multiplication. """
        return x * multiplier
    return multiplier_function
