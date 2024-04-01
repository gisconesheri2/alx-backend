import csv
import math
from typing import List, Dict


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
        """Returns a slice of a dataset corresponding
        to @page_size from specified @page
        """
        assert type(page) is int
        assert type(page_size) is int
        assert page_size > 0
        assert page > 0
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        data_set = self.dataset()
        try:
            pages = data_set[start_index: end_index]
            return pages
        except IndexError:
            return []
