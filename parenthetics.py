#!/usr/bin/env python


"""Proper Parenthetics
Return 1 if the string is "open" (there are open parens that are not closed)

Return 0 if the string is "balanced" (there are an equal number of open and
closed parentheses in the string)

Return -1 if the string is "broken" (a closing parens has not been proceeded
by one that opens)
"""


def parenthetics(inp):
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
    elif count <= -1:
        return -1
    else:
        return 0
