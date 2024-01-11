#!/usr/bin/env python3
"""This function taks list and retuns tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This function squares int inputs"""
    return k, v ** 2
