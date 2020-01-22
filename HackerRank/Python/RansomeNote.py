#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    wordDict = {}
    answer = 'Yes'
    for word in magazine:
        if word in wordDict:
            wordDict[word] = wordDict[word] + 1
        else:
            wordDict[word] = 1
    for word in note:
        if word not in wordDict:
            answer = 'No'
            break
        else:
            if wordDict[word] < 1:
                answer = 'No'
                break
            else:
                wordDict[word] = wordDict[word] - 1
    print(answer)

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
