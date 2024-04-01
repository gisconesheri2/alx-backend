#!/usr/bin/env python3
"""calculate start and end index for pagination purposes
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """calculate start and end index for pagination purposes
    """
    assert type(page) is int
    assert page > 0
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
