import sys
n = int(sys.stdin.readline())
nums = list(map(int, [sys.stdin.readline().strip() for _ in range(n)]))

def qsort(a, l: int, r: int):
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

qsort(nums, 0, n - 1)
print('\n'.join(map(str, nums)))