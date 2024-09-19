import sys
from typing import MutableSequence

def improved_bubble_sort(arr: MutableSequence):
  n = len(arr)
  for i in range(n - 1):
    cnt = 0
    for j in range(n - 1, i, -1):
      if arr[j - 1] <= arr[j]:
        continue
      arr[j - 1], arr[j] = arr[j], arr[j - 1]
      cnt += 1
    if cnt == 0:
      break

arr = list(map(int, sys.stdin.readline().strip().split(' ')))
print()
print('prev: ', arr)
print('sorted: ', improved_bubble_sort(arr))