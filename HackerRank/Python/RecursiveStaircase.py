#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
def stepPerms(n):
    return stepMemo(n, {}, '')

def stepMemo(n, memo, s):
    string = f'{n}:{s}'
    if n == 0:
        return 1
    if n < 0:
        return 0
    if string in memo:
        return memo[string]
    result = stepMemo(n-3, memo, "3") + stepMemo(n-2, memo, "2") + stepMemo(n-1, memo, "1")
    memo[string] = result
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
