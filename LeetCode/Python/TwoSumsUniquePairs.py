def twoSumUniquePairs(arr, target):
  sumSet = set()
  uniqueSet = set()
  for num in arr:
    if target-num in sumSet:
      uniqueSet.add(num)
    else:
      sumSet.add(num)
  print(len(uniqueSet))

twoSumUniquePairs([1,2,3,4,5, 2, 5, 3, 3, 1, 5, 2, 4], 6)