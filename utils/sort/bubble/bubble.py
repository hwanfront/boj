import sys
from typing import MutableSequence

def bubble_sort(arr: MutableSequence):
  n = len(arr)
  for i in range(n - 1):
    for j in range(n - 1, i, -1):
      if arr[j - 1] <= arr[j]:
        continue
      arr[j - 1], arr[j] = arr[j], arr[j - 1]

arr = list(map(int, sys.stdin.readline().strip().split(' ')))
print()
print('prev: ', arr)
bubble_sort(arr)
print('sorted: ', arr)