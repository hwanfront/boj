import sys
n = int(sys.stdin.readline())
nums = list(map(int, [sys.stdin.readline().strip() for _ in range(n)]))

def qsort(a, l: int, r: int):
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

  if l < pr: qsort(a, l, pr)
  if pl < r: qsort(a, pl, r)

qsort(nums, 0, n - 1)
print('\n'.join(map(str, nums)))