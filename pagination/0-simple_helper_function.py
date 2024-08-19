#!/usr/bin/env python3
"""
    Defines afunction named index_range that takes two integer arguments
    page and page_size and returns a tuple of size containing a start index
    and corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
"""


def index_range(page, page_size):
    """
        Takes two integer arguments : page and page_size.

        Args:
            page (int): The start index of the page.
            page_size (int): The range of indexes.

        Returns:
            A tuple of size two containing a start index and an end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
