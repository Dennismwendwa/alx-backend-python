#!/usr/bin/env python3
"""Duck typing iterable objects"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This function uses list compression to return tuples"""
    return [(i, len(i)) for i in lst]
