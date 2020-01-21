#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    if len(prices) == 0:
        return 0
    sortedPrices = sorted(prices)
    items = 0
    if sortedPrices[0] > k:
        return 0
    for price in sortedPrices:
        k -= price
        if k <= 0:
            break
        items+=1
    return items

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
