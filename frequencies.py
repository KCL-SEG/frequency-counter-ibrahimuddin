"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    string_items = [str(item) for item in items]

    frequencies = {}
    for item in string_items:
        if item not in frequencies.keys():
            frequencies[str(item)] = 1
        else:
            frequencies[str(item)] = frequencies[item]+1
    return frequencies

print(frequencies([100, 'Hello', '100', '100', 100]))
