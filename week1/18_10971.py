import sys
def go(now, cost, cnt, start):
  global result
  if cost >= result: return
  if v[start] != 1 and cnt == n - 1 and w[now][start] != 0:
    result = min(result, cost + w[now][start])
    return

  for next in range(0, n):
    if start == next: continue
    if w[now][next] == 0: continue
    if v[next] == 1: continue
    v[next] = 1
    go(next, cost + w[now][next], cnt + 1, start)
    v[next] = 0

n = int(sys.stdin.readline().strip())
w = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(n)]
v = [0 for _ in range(n)]
result = sys.maxsize
for i in range(n):
  go(i, 0, 0, i)
print(result)