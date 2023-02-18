#!/usr/bin/env python3
""" implements class server"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """ returns a tuple of size 2 containing a start and end index"""
    pg = page * page_size
    return (pg - page_size, page * page_size)


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
        """gets correct page size of the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        self.dataset()
        rows = index_range(page, page_size)
        if page > len(self.__dataset) or page_size > len(self.__dataset):
            return []
        return self.__dataset[rows[0]:rows[1]]
