#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> dict:
        """ Returns a dictionary with the following key-value pairs:
                index: the current start index of the return page.
                data: the actual page of the dataset.
                page_size: the current page size.
                next_index: the next index to query with.
        """
        indexed_data = self.indexed_dataset()
        total_items = len(indexed_data)

        if index is None:
            index = 0

        assert isinstance(index, int) and 0 <= index < total_items

        data = []
        current_index = index
        count = 0

        while count < page_size and current_index < total_items:
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                count += 1
            current_index += 1

        next_index = current_index if current_index < total_items else None

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
