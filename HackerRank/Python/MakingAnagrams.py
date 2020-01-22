#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    arr = [0 for i in range(26)]
    deletions = 0
    for c in a.lower():
        index = ord(c) - ord('a')
        arr[index] = arr[index] + 1
    for c in b.lower():
        index = ord(c) - ord('a')
        arr[index] = arr[index] - 1
    for count in arr:
        deletions+= abs(count)
    return deletions

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
