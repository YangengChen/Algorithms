#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    rotations = d % len(a)
    res = [0 for i in range(len(a))]
    for i in range(len(a)):
        index = len(a) - rotations
        if i+index >= len(a):
            newIndex = (i + index) % len(a)
            res[newIndex] = a[i]
        else:
            res[i+index] = a[i]
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
