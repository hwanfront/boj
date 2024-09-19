import sys
from typing import MutableSequence

def insertion_sort(arr: MutableSequence):
  for i in range(1, len(arr)):
    j = i
    tmp = arr[i]
    while j > 0 and arr[j - 1] > tmp:
      arr[j] = arr[j - 1]
      j -= 1
    arr[j] = tmp

arr = list(map(int, sys.stdin.readline().strip().split(' ')))
print()
print('prev: ', arr)
insertion_sort(arr)
print('sorted: ', arr)