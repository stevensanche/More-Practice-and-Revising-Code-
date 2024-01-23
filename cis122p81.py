"""
CIS 122 Spring 2022 Project 8-1
Testing and Debugging

Author: Steven Sanchez-Jimenez

Credit: CIS 122 Resources, Office Hours

Practice testing and debugging code.
More practice revising code.
"""

import doctest


# (0)
def count_vowels(s):
    """(s: str) -> int
    Return number of vowels in s.

    >>> count_vowels('The quick brown fox')
    5
    >>> count_vowels('University of Oregon')
    8
    >>> count_vowels('Hello, World')
    3
    >>> count_vowels('Python')
    1
    >>> count_vowels('CCC')
    0

    more examples of use/test cases go here
    """
    vowels = 'aeiou'
    ctr = 0
    for ch in s:
        ch = ch.lower()
        if ch in vowels:
            ctr += 1
    return ctr



# (1)
def my_average(dataset):
    """(dataset: str) -> float

    Returns average of values in non-empty input string
    of digits. Zeros should be ignored.  Return 0
    if there is no real data.

    >>> my_average('23')
    2.5
    >>> my_average('203')
    2.5

    more examples of use/test cases go here
    """
    count = 0
    total = 0
    for value in dataset:
        if value != '0':
            total += int(value)
            count += 1
    avg = total / count
    return avg


#  (2) Example from text Ch. 8 Debugging

def is_reverse(word1, word2):
    """(word1: str, word2: str) -> bool

    compare two words and return True if
    one is the reverse of the other

    >>> is_reverse('abc', 'cba')
    True
    >>> is_reverse('a', 'a')
    True
    >>> is_reverse('abcc', 'abcc')
    False
    >>> is_reverse('yes', 'no')
    False
    >>> is_reverse('abb', 'bbb')
    False
    >>> is_reverse('abc', 'zba')
    False
    """
    if len(word1) != len(word2):
        return False
    i = 0
    j = len(word2) - 1
    while j >= 0:
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1
    return True


def main():
    doctest.testmod()


if __name__ == "__main__":
    main()
