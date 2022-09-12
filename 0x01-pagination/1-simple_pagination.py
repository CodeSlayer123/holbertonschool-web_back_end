#!/usr/bin/env python3
"""Task 1 Task 1 Task 1 Task 1 Task 1"""
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Task 1 Task 1 Task 1 Task 1 Task 1"""

    return (page_size * (page - 1), page_size * page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """inits the class Server"""
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
        "function that gets page and returns in form of list"
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        rows = self.dataset()
        page_range = index_range(page, page_size)
        new_list = []
        x = page_range[0]
        y = page_range[1]
        if x > len(rows) or y > len(rows):
            return new_list
        for i in range(x, y):
            new_list.append(rows[i])
        return new_list
