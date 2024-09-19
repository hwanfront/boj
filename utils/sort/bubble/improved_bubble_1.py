import sys
from typing import MutableSequence

def improved_bubble_sort(arr: MutableSequence):
  n = len(arr)
  k = 0
  while k < n - 1:
    last = n - 1
    for j in range(n - 1, k, -1):
      if arr[j - 1] <= arr[j]:
        continue
      arr[j - 1], arr[j] = arr[j], arr[j - 1]
      last = j
    k = last


arr = list(map(int, sys.stdin.readline().strip().split(' ')))
print()
print('prev: ', arr)
improved_bubble_sort(arr)
print('sorted: ', arr)