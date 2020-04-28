#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.
    Prototype: def canUnlockAll(boxes)
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
"""

def canUnlockAll(boxes):
    """
    method that determines if all the boxes can be opened
    """
    keys = set(boxes[0])
    pending = list(range(1, len(boxes)))
    i = 0
    while len(pending) != 0:
        if i in keys and i in pending:
            keys.update(set(boxes[i]))
            pending.remove(i)
            i = 0
        i += 1
        if i == len(boxes):
            return False
    return True