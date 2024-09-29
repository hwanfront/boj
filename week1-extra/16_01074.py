import sys
n, r, c = tuple(map(int, sys.stdin.readline().strip().split(' ')))

def z(n, s, r, c):
  if n == 1:
    return s
  mid = n // 2
  if r < mid and c < mid:
    return z(n // 2, s, r, c)
  if r < mid and mid <= c:
    return z(n // 2, s + mid ** 2, r, c - mid)
  if mid <= r and c < mid:
    return z(n // 2, s + (mid ** 2) * 2, r - mid, c)
  return z(n // 2, s + (mid ** 2) * 3, r - mid , c - mid)

print(z(2 ** n, 0, r, c))