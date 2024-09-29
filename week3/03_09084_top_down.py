import sys
sys.setrecursionlimit(10**5)
t = int(sys.stdin.readline().strip())
result = []

def go(amount, k):
  if amount < 0:
    return 0
  if amount == 0:
    return 1
  if dp[k][amount] > -1:
    return dp[k][amount]
  
  total = 0
  for i in range(k, len(coins)):
    total += go(amount - coins[i], i)

  dp[k][amount] = total
  return dp[k][amount]

for _ in range(t):
  n = int(sys.stdin.readline().strip())
  coins = tuple(map(int, sys.stdin.readline().strip().split()))
  value = int(sys.stdin.readline().strip())
  dp = [[-1] * (value + 1) for _ in range(n)]
  
  result.append(go(value, 0))

print('\n'.join(map(str, result)))