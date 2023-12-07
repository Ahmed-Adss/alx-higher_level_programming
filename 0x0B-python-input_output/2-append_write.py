#!/usr/bin/python3
"""
function that appends string
"""


def append_write(filename="", text=""):
    """returns of number of characters added:"""
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
