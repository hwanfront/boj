import sys
n = int(sys.stdin.readline())
MOD = 15746

dp = [0] * n
if n == 1:
  print(1)
  exit()
if n == 2:
  print(2)
  exit()
dp[0] = 1
dp[1] = 2
for i in range(2, n):
  dp[i] = (dp[i - 1] + dp[i - 2]) % MOD

print(dp[n - 1])