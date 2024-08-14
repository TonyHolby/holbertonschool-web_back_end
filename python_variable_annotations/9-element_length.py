#!/usr/bin/env python3
"""
    Defines a function named element_length that takes a list of
    iterable elements and returns a list of tuples.
"""
from typing import List, Tuple, Iterable


def element_length(lst: Iterable[str]) -> List[Tuple[str, int]]:
    """ Returns the values with the appropriate types. """
    return [(i, len(i)) for i in lst]
