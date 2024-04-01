#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


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
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Deletion-resilient hypermedia pagination
        """
        idx_ds = self.indexed_dataset()
        assert type(index) is int
        assert index < len(idx_ds) - 1

        res = {}
        res['index'] = index
        res['data'] = []
        current_pos = index
        while len(res['data']) < page_size:
            idx_data = idx_ds.get(current_pos, None)
            if idx_data is not None:
                res['data'].append(idx_data)
            current_pos += 1
        res['page_size'] = len(res['data'])
        res['next_index'] = current_pos

        return res
