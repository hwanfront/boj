import sys
n = int(sys.stdin.readline().strip())
matrixs = [tuple(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(n)]
data = [0] * (n + 1)
dp = [[0] * (n + 1) for _ in range(n + 1)]
data[0] = matrixs[0][0]
for i in range(n):
  data[i + 1] = matrixs[i][1]
  
for i in range(n - 1):
  for j in range(i, n - 1):
    s = j - i
    e = j + 2
    for k in range(s + 1, e):
      val = dp[s][k] + dp[k][e] + (data[s] * data[k] * data[e])
      if dp[s][e] == 0:
        dp = val
        continue
      if dp[s][e] > val:
        dp[s][e] = val

print(dp[0][n])
