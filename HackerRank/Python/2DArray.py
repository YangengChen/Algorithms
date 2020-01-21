#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    maxHourglassSum = -sys.maxsize
    for j in range(1,5):
        for k in range(1,5):
            thisSum =  (arr[j-1][k-1] + arr[j-1][k] + arr[j-1][k+1]  
                                  + arr[j][k]   +
                    arr[j+1][k-1] + arr[j+1][k] + arr[j+1][k+1])
            print(f'{maxHourglassSum} {thisSum}')
            maxHourglassSum = max(maxHourglassSum, thisSum)
    return maxHourglassSum 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
