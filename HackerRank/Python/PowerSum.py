#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the powerSum function below.
def powerSum(X, N):
    a = [pow(i,N) for i in range(1,40)]
    return findNumOfWays(X, a, len(a)-1)

def findNumOfWays(num, arr, i):
    if num == 0:
        return 1
    elif num < 0:
        return 0
    elif i < 0:
        return 0
    else:
        return findNumOfWays(num - arr[i], arr, i-1) + findNumOfWays(num, arr, i-1)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X, N)

    fptr.write(str(result) + '\n')

    fptr.close()
