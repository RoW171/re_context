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

"""Utility for creating regex-patterns with a context manager."""

from re import compile
from typing import Optional, Union, Pattern as RE_Pattern

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
    """RegEx pattern helper class."""

    _pattern_string: str

    def __init__(self, start_string: str = r''):
        self._pattern_string = r'' + start_string

    def __repr__(self) -> str:
        return rf're_context.Pattern{self.pattern_string}'

    def __str__(self) -> str:
        return self.pattern_string

    def __enter__(self) -> 'Pattern':  # not using __future__.annotations, to work with <3.7
        """contextmanager startup."""
        return self

    def __exit__(self, exc_type: Optional[Exception], exc_val: Optional[Exception], exc_tb: Optional[Exception]):
        """contextmanager cleanup."""
        pass

    def __iadd__(self, other: Union[str, 'Pattern']) -> 'Pattern':
        """Augmented Addition; For (raw)strings or re_context.Patterns as others only."""
        if isinstance(other, Pattern): other = other.pattern_string
        self.pattern_string += other
        return self

    @property
    def compiled(self) -> RE_Pattern:
        """The re.compiled pattern_string."""
        return compile(self.pattern_string)

    @property
    def pattern_string(self) -> str:
        """The string representing the pattern."""
        return self._pattern_string

    @pattern_string.setter
    def pattern_string(self, new_string: str):
        self._pattern_string = new_string

    def clear(self) -> 'Pattern':
        """Clear the pattern_string; Returns self to to reuse in a contextmanager."""
        self.pattern_string = r''
        return self

    def add(self, char: str) -> None:
        """Add any data to the pattern_string. Usage of rawstrings highly advudes."""
        self.pattern_string += char

    def add_any_char(self) -> None:
        """Add r'.' to pattern_string. Represents any character."""
        self.pattern_string += ANY_CHAR

    def add_digit(self) -> None:
        r"""Add r'\d' to pattern_string. Represents any digit."""
        self.pattern_string += DIGIT

    def add_not_digit(self) -> None:
        r"""Add r'\D' to pattern_string. Represents any character BUT digits."""
        self.pattern_string += NOT_DIGIT

    def add_word(self) -> None:
        r"""Add r'\w' to pattern_string. Represents any letter."""
        self.pattern_string += WORD

    def add_not_word(self) -> None:
        r"""Add r'\W' to pattern_string. Represents any character BUT a letter."""
        self.pattern_string += NOT_WORD

    def add_whitespace(self) -> None:
        r"""Add r'\s' to pattern_string. Represents any whitespace."""
        self.pattern_string += WHITESPACE

    def add_not_whitespace(self) -> None:
        r"""Add r'\S' to pattern_string. Represents any character BUT a whitespaces."""
        self.pattern_string += NOT_WHITESPACE

    def add_word_boundry(self) -> None:
        r"""Add r'\b' to pattern_string. Represents any range of word-characters
        seperated by non-word-characters."""
        self.pattern_string += WORD_BOUNDRY

    def add_not_word_boundry(self) -> None:
        r"""Add r'\B' to pattern_string. Opposite Pattern.add_word_boundry()."""
        self.pattern_string += NOT_WORD_BOUNDRY

    def add_string_begin(self) -> None:
        """Add r'^' to pattern_string. Represents the start of a string."""
        self.pattern_string += STRING_BEGIN

    def add_string_end(self) -> None:
        """Add r'$' to pattern_string. Represents the end of a string."""
        self.pattern_string += STRING_END

    def add_zero_or_more(self) -> None:
        """Add r'*' to pattern_string. Represents zero or more characters."""
        self.pattern_string += ZERO_OR_MORE

    def add_one_or_more(self) -> None:
        """Add r'+' to pattern_string. Represents one or more characters."""
        self.pattern_string += ONE_OR_MORE

    def add_zero_or_one(self) -> None:
        """Add r'?' to pattern_string. Represents zero or one character."""
        self.pattern_string += ZERO_OR_ONE

    def add_match(self, *match) -> None:
        """Add a match to pattern_string. Takes any number above zero
        string arguments to put within the match."""
        self.pattern_string += _MATCH.format(''.join(match))

    def add_not_match(self, *not_match) -> None:
        """Add ^-match to pattern_string. Basically same usage as add_not_match."""
        self.pattern_string += _NOT_MATCH.format(''.join(not_match))

    def add_group(self, *group) -> None:
        """Add group to pattern_string. Represents any character. Takes any number
        above zero string arguments to put within the match."""
        self.pattern_string += _GROUP.format(''.join(group))

    def add_exact_number(self, number: int) -> None:
        """Add a exact number of characters to pattern_string."""
        self.pattern_string += _EXACT_NUMBER.format(number)

    def add_range_of_numbers(self, start: int, end: int) -> None:
        """Add a range of chatacters to pattern_string."""
        self.pattern_string += _RANGE_OF_NUMBERS.format(start, end)


if __name__ == '__main__': pass
