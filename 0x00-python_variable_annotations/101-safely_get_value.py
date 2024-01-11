#!/usr/bin/env python3
"""Type annotation in dict object"""
from typing import Mapping, Any, TypeVar, Union


T = TypeVar("T")
Defa = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Defa = None
                     ) -> Union[Any, T]:
    """This function returns the key of dict if available"""
    if key in dct:
        return dct[key]
    else:
        return default
