#!/usr/bin/env python3
"""
    Defines a class named Server that returns a dictionary containing
    the following key-value pairs:
        page_size: the length of the returned dataset page.
        page: the current page number.
        data: the dataset page.
        next_page: number of the next page.
        prev_page: number of the previous page.
        total_pages: the total number of pages in the dataset as an integer.
"""
import csv
import math
from typing import List, Dict, Optional


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """ Verifies that both arguments are integers greater than 0
            and returns the appropriate page of the dataset.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        start_index, end_index = self.index_range(page, page_size)
        return dataset[start_index:end_index]

    def index_range(self, page: int, page_size: int) -> tuple:
        """ Returns the correct indexes to paginate the dataset correctly. """
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        return (start_index, end_index)

    def get_hyper(
            self, page: int = 1, page_size: int = 10
            ) -> Dict[str, Optional[int]]:
        """ Returns a dictionary containing pagination info. """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        hypermedia = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }

        return hypermedia
