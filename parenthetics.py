#!/usr/bin/env python


def parenthetics(inp):
    """Checks for balanced parenthetic usage in a given input

    Returns 1 if the string has open parenthetics that are not properly closed.
    Returns 0 if the string is balanced.
    Returns -1 if the string has closing parentheses before opening.

    """
    count = 0
    for char in inp:
        if char == "(":
            count += 1
        if char == ")":
            count -= 1
            if count < 0:
                return -1
    if count >= 1:
        return 1
    else:
        return 0
