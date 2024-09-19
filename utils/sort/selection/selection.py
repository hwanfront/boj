import sys
from typing import MutableSequence

# straight selection sort
def selection_sort(arr: MutableSequence):
  for i in range(len(arr) - 1):
    min_idx = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[min_idx]: 
        min_idx = j
    arr[min_idx], arr[i] = arr[i], arr[min_idx]

arr = list(map(int, sys.stdin.readline().strip().split(' ')))
print()
print('prev: ', arr)
selection_sort(arr)
print('sorted: ', arr)