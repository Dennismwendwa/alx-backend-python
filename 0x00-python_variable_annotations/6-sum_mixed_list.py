#!/usr/bin/env python3
"""This function sum mixed list of ints and floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This function sum all elements of a list"""
    return sum(mxd_lst)
