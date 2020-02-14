schedules1 = [
  [[0, 3], [3, 4], [6, 8], [9, 10], [10, 13], [13, 15], [17, 19], [20, 22], [22, 24]],
  [[0, 2], [2, 4], [9, 10], [10, 12], [16, 17], [19, 21], [23, 24]],
  [[4, 5], [5, 8], [14, 15], [15, 16], [18, 19], [19, 22]],
  [[6, 9], [9, 11], [12, 15], [15, 16], [21, 23], [23, 24]],
  [[0, 1], [1, 4], [4, 7], [7, 8], [8, 10], [10, 13], [13, 14], [15, 18], [19, 21]]
]
# /*
#   Expected Output: The largest meeting you can have is with 3 people between 16 and 19.
# */
schedules2 = [
  [[0, 3], [3, 4], [6, 8], [9, 10], [10, 13], [13, 15], [16, 19], [20, 22], [22, 24]],
  [[0, 2], [2, 4], [9, 10], [10, 12], [19, 21], [23, 24]],
  [[4, 5], [5, 8], [14, 15], [19, 22]],
  [[6, 9], [9, 11], [12, 15], [15, 16], [21, 23], [23, 24]],
  [[0, 1], [1, 4], [4, 7], [7, 8], [8, 10], [10, 13], [13, 14], [15, 19], [19, 21]]
]
# /*
#   Expected Output: The largest meeting you can have is with 3 people between 21 and 24.
# // */
schedules3 = [
  [[0, 3], [3, 4], [6, 8], [9, 10], [10, 13], [13, 15], [17, 19], [20, 22], [22, 24]],
  [[0, 2], [2, 4], [9, 10], [10, 12], [16, 17], [19, 21]],
  [[4, 5], [5, 8], [14, 15], [15, 16], [18, 19], [19, 21]],
  [[6, 9], [9, 11], [12, 15], [15, 16], [21, 23], [23, 24]],
  [[0, 1], [1, 4], [4, 7], [7, 8], [8, 10], [10, 13], [13, 14], [15, 18], [19, 21]]
]

import sys

def largestMeeting(schedules):
  busyArr = ["" for i in range(24)]
  for i in range(len(schedules)):
    for j in range(len(schedules[i])):
      start = schedules[i][j][0]
      end = schedules[i][j][1]
      for k in range(start, end):
        busyArr[k] += f'{i}'
    
  maxLen = -sys.maxsize
  maxCount = -sys.maxsize
  currLen = 0
  start = 0
  end = 1
  for i in range(0, len(busyArr)):
    currLen += 1
    numAvail = len(schedules) - len(busyArr[i])
    if i+1 == len(busyArr):
      if maxCount < numAvail:
        maxCount = numAvail
        end = i + 1
        start = end - currLen
        maxLen = currLen
      elif maxCount == numAvail:
        if maxLen < currLen:
          end = i + 1
          start = end - currLen
          maxLen = currLen
      break
        
    curr = busyArr[i]
    next = busyArr[i+1] 
    if curr != next:
      if maxCount < numAvail:
        maxCount = numAvail
        end = i + 1
        start = end - currLen
        maxLen = currLen
      elif maxCount == numAvail:
        if maxLen < currLen:
          end = i + 1
          start = end - currLen
          maxLen = currLen
      currLen = 0
  print(f'largest schedule with {maxCount} people at [{start},{end}]')
  
largestMeeting(schedules1)
largestMeeting(schedules2)
largestMeeting(schedules3)