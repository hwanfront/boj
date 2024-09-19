import sys
from typing import MutableSequence
def partition(arr: MutableSequence, l: int, r: int):
  pivot = arr[r]
  i = l - 1
  for j in range(l, r):
    if arr[j] < pivot:
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
  
  arr[i + 1], arr[r] = arr[r], arr[i + 1]
  return i + 1

def qsort(arr, l, r):
  if l < r:
    pivot = partition(arr, l, r)
    qsort(arr, l, pivot - 1)
    qsort(arr, pivot + 1, r)

arr = list(map(int, sys.stdin.readline().strip().split(' ')))
print()
print('prev: ', arr)
qsort(arr, 0, len(arr) - 1)
print('sorted: ', arr)