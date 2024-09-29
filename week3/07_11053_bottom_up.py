import sys
n = int(sys.stdin.readline().strip())
data = tuple(map(int, sys.stdin.readline().strip().split(' ')))
result = 1

dp = [1] * (n)

for i in range(1, n):
  for j in range(i - 1, -1, -1):
    if data[j] < data[i]:
      if dp[i] <= dp[j]:
        dp[i] = dp[j] + 1
      if result < dp[i]:
        result = dp[i]
        break

print(dp)
print(result)