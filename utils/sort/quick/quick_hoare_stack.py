import sys
from typing import MutableSequence
def qsort(a: MutableSequence, l: int, r: int):
  range = []

  range.append((l, r))

  while len(range) != 0:
    l, r = range.pop()
    pl = l
    pr = r
    pivot = a[(pl + pr) // 2]
    while pl <= pr:
      while a[pl] < pivot: pl += 1
      while pivot < a[pr]: pr -= 1
      if pl <= pr:
        a[pl], a[pr] = a[pr], a[pl]
        pl += 1
        pr -= 1

    if l < pr: range.append((l, pr))
    if pl < r: range.append((pl, r))

arr = list(map(int, sys.stdin.readline().strip().split(' ')))
print()
print('prev: ', arr)
qsort(arr, 0, len(arr) - 1)
print('sorted: ', arr)