import sys
from typing import MutableSequence

def shaker_sort(arr: MutableSequence):
  left = 0
  right = len(arr) - 1
  last = right
  while left < right:
    for i in range(right, left, -1):
      if arr[i - 1] > arr[i]:
        arr[i - 1], arr[i] = arr[i], arr[i - 1]
        last = i
    left = last

    for i in range(left, right):
      if arr[i] > arr[i + 1]:
        arr[i] , arr[i + 1] = arr[i + 1], arr[i] 
        last = i
    right = last

arr = list(map(int, sys.stdin.readline().strip().split(' ')))
print()
print('prev: ', arr)
shaker_sort(arr)
print('sorted: ', shaker_sort(arr))