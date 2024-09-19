import sys
from typing import MutableSequence

def shell_sort(arr: MutableSequence):
  h = 1

  while h < len(arr) // 9:
    h = h * 3 + 1

  while h > 0:
    for i in range(h, len(arr)):
      j = i - h
      tmp = arr[i]
      while j >= 0 and arr[j] > tmp:
        arr[j + h] = arr[j]
        j -= h
      arr[j + h] = tmp
    h //= 3

arr = list(map(int, sys.stdin.readline().strip().split(' ')))
print()
print('prev: ', arr)
shell_sort(arr)
print('sorted: ', arr)