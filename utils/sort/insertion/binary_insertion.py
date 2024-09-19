import sys
from typing import MutableSequence

def binary_search(arr, i, key):
  l = 0
  r = i - 1
  while l < r:
    m = (l + r) // 2
    if arr[m] < key:
      l = m + 1
    else:
      r = m - 1
  if arr[l] < key:
    return l + 1
  return l
  
def binary_insertion_sort(arr: MutableSequence):
  for i in range(1, len(arr)):
    key = arr[i]
    pos = binary_search(arr, i, key)
    for j in range(i, pos, -1):
      arr[j] = arr[j - 1]
    arr[pos] = key

arr = list(map(int, sys.stdin.readline().strip().split(' ')))
print()
print('prev: ', arr)
binary_insertion_sort(arr)
print('sorted: ', arr)