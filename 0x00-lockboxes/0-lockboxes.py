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
    boxes.sort()
    cont = 0

    for index, i in enumerate(boxes, start=1):
            if index < len(boxes) and boxes[index][0] == index:
                print(boxes[index][0])
                cont += 1

    if cont == len(boxes)-1:
        return(True)
    else:
        return(False)