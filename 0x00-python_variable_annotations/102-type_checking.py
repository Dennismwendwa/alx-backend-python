#!/usr/bin/env python3
"""Checking the type using mypy"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """This function returns list of the zoomed_in"""
    zoomed_in: List = [
        item for item in lst
        for _ in range(int(factor))
    ]
    return zoomed_in


array = (12, 72, 91)
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
