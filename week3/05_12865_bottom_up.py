import sys
n, k = tuple(map(int, sys.stdin.readline().strip().split(' ')))
items = [tuple(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(n)]

dp = [0] * (k + 1)

for w, v in items:
  for i in range(k, w - 1, -1):
    dp[i] = max(dp[i], dp[i - w] + v)
print(dp[k])