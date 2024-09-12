import sys
n = int(sys.stdin.readline().strip())
aa = list(map(int, sys.stdin.readline().strip().split(' ')))
m = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split(' ')))
result = [0] * m

aa.sort()

def bs(n, aa, to, i):
  l = 0
  r = n - 1
  while l <= r:
    mid = (l + r) // 2
    if aa[mid] == to:
      result[i] = 1
      return 
    if aa[mid] < to:
      l = mid + 1
    if aa[mid] > to:
      r = mid - 1
  
for i in range(m):
  num = nums[i]
  bs(n, aa, num, i)

print('\n'.join(list(map(str, result))))