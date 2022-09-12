#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Task 2 Task 2 Task 2 Task 2 Task 2"""

    return (page_size * (page - 1), page_size * page)


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

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Gets hyper index and returns dictionary"""
        assert index > 0
        assert index < len(self.dataset())
        return {
            "index": index,
            "next_index": index + page_size,
            "page_size": page_size,
            "data": self.get_page(index / page_size, page_size)
            }

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        "function that gets page and returns in form of list"
        assert page > 0
        assert isinstance(page_size, int)
        rows = self.dataset()
        page_range = index_range(page, page_size)
        new_list = []
        x = int(page_range[0])
        y = int(page_range[1])
        if x > len(rows) or y > len(rows):
            return new_list
        for i in range(x, y):
            new_list.append(rows[i])
        return new_list
