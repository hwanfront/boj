import sys
s1 = sys.stdin.readline().strip()
s2 = sys.stdin.readline().strip()

dp = [[0] * len(s1) for _ in range(len(s2))]

if s1[0] == s2[0]:
  dp[0][0] = 1

for x in range(1, len(s1)):
  if s1[x] == s2[0]:
    dp[0][x] = 1
  else:
    dp[0][x] = dp[0][x - 1]
for y in range(1, len(s2)):
  if s2[y] == s1[0]:
    dp[y][0] = 1
  else:
    dp[y][0] = dp[y - 1][0]

for y in range(1, len(s2)):
  for x in range(1, len(s1)):
    if s2[y] == s1[x]:
      dp[y][x] = max(dp[y][x - 1], dp[y - 1][x], dp[y - 1][x - 1] + 1)
      continue
    dp[y][x] = max(dp[y][x - 1], dp[y - 1][x], dp[y - 1][x - 1])

print(max(dp[len(s2) - 1]))