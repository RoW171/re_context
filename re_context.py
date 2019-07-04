#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'Robin "r0w" Weiland'
__credits__ = ('Robin Weiland',)
__copyright__ = 'Copyright 2019, Robin Weiland'

__date__ = '2019-07-03'
__version__ = '0.0.1'
__license__ = 'MIT'

__all__ = ('Pattern', 'ANY_CHAR', 'DIGIT', 'NOT_DIGIT', 'WORD', 'NOT_WORD', 'WHITESPACE',
           'NOT_WHITESPACE', 'WORD_BOUNDRY', 'NOT_WORD_BOUNDRY', 'STRING_BEGIN',
           'STRING_END', 'ZERO_OR_MORE', 'ONE_OR_MORE', 'ZERO_OR_ONE', 'EITHER_OR',)

"""utility for creating regex-patterns with a context manager"""

ANY_CHAR: str = r'.'
DIGIT: str = r'\d'
NOT_DIGIT: str = r'\D'
WORD: str = r'\w'
NOT_WORD: str = r'\W'
WHITESPACE: str = r'\s'
NOT_WHITESPACE: str = r'\S'

WORD_BOUNDRY: str = r'\b'
NOT_WORD_BOUNDRY: str = r'\B'
STRING_BEGIN: str = r'^'
STRING_END: str = r'$'

ZERO_OR_MORE: str = r'*'
ONE_OR_MORE: str = r'+'
ZERO_OR_ONE: str = r'?'  # rename 'BINARY' ?

EITHER_OR: str = r'|'
# The following strings need to be formatted add are not recommended
# to directly use. Rather work with the functions further below
_MATCH: str = r'[{}]'
_NOT_MATCH: str = r'[^{}]'
_GROUP: str = r'({})'
_EXACT_NUMBER: str = r'{{{}}}'
_RANGE_OF_NUMBERS: str = r'{{{},{}}}'


class Pattern:
    """RegEx pattern helper class"""
    _pattern_string: str

    def __init__(self, start_string: str = r''):
        self._pattern_string = r'' + start_string

    def __repr__(self) -> str:
        return rf're_context.Pattern{self.pattern_string}'

    def __str__(self) -> str:
        return self.pattern_string

    @property
    def pattern_string(self) -> str:
        """The string representing the pattern"""
        return self._pattern_string

    @pattern_string.setter
    def pattern_string(self, new_string: str):
        self._pattern_string = new_string


if __name__ == '__main__': pass
