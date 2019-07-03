#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Robin "r0w" Weiland'
__credits__ = ('Robin Weiland',)
__copyright__ = 'Copyright 2019, Robin Weiland'

__date__ = '2019-07-03'
__version__ = '0.0.1'
__license__ = 'MIT'

__all__ = ('Pattern',)

"""utility for creating regex-patterns with a context manager"""


class Pattern:
    """RegEx pattern helper class"""
    _pattern_string: str

    def __init__(self, start_string: str = r''): self._pattern_string = r'' + start_string

    def __repr__(self) -> str: return rf're_context.Pattern{self.pattern_string}'

    def __str__(self) -> str: return self.pattern_string

    @property
    def pattern_string(self) -> str: return self._pattern_string

    @pattern_string.setter
    def pattern_string(self, new_string: str): self._pattern_string = new_string


if __name__ == '__main__': pass
