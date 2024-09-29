import sys
t = int(sys.stdin.readline().strip())
result = []
for _ in range(t):
  n = int(sys.stdin.readline().strip())
  coins = tuple(map(int, sys.stdin.readline().strip().split()))
  value = int(sys.stdin.readline().strip())
  dp = [0] * (value + 1)
  for i in range(coins[0], value + 1, coins[0]):
    dp[i] = 1

  for idx in range(1, n):
    coin = coins[idx]
    if coin > value:
      continue
    dp[coin] += 1
    for i in range(coin, value + 1):
      dp[i] += dp[i - coin]
  result.append(dp[value])

print('\n'.join(map(str, result)))