#!/usr/bin/env python3
"""This function returns a callable"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This function returns a callable objects"""
    def multiplier_fun(m: float) -> float:
        return m * multiplier
    return multiplier_fun
