import sys
from typing import MutableSequence
import bisect

def binary_insertion_sort(arr: MutableSequence):
  for idx in range(1, len(arr)):
    bisect.insort(arr, arr.pop(idx), 0, idx)

arr = list(map(int, sys.stdin.readline().strip().split(' ')))
print()
print('prev: ', arr)
binary_insertion_sort(arr)
print('sorted: ', arr)