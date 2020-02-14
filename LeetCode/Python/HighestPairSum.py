'''
Given a list of positive integers nums and an int target, 
return indices of the two numbers such that they add up to a target - 30.

Conditions:

You will pick exactly 2 numbers.
You cannot pick the same element twice.
If you have muliple pairs, select the pair with the largest number.
Example 1:

Input: nums = [1, 10, 25, 35, 60], target = 90
Output: [2, 3]
Explanation:
nums[2] + nums[3] = 25 + 35 = 60 = 90 - 30
'''
import sys

def highestPairSum(arr, target):
  targetNum = target - 30
  sumMap = {}
  maxNum = -sys.maxsize
  for i in range(len(arr)):
    if targetNum - arr[i] in sumMap:
      maxNum = max(maxNum, max(targetNum-arr[i], arr[i]))
    sumMap[arr[i]] = i 
  print(f'[{sumMap[targetNum-maxNum]}, {sumMap[maxNum]}]')

highestPairSum([1, 10, 25, 35, 60], 90)