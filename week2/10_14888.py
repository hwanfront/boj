import sys
n = int(sys.stdin.readline().strip())
aa = list(map(int, sys.stdin.readline().strip().split(' ')))
op = list(map(int, sys.stdin.readline().strip().split(' ')))
mn = 10 ** 9
mx = -(10 ** 9)

def dfs(now, res):
  global mx, mn
  if now == n:
    mn = min(res, mn)
    mx = max(res, mx)
    return
  
  for i in range(0, 4):
    if op[i] == 0:
      continue
    op[i] -= 1
    if i == 0:
      dfs(now + 1, res + aa[now])
    elif i == 1:
      dfs(now + 1, res - aa[now])
    elif i == 2:
      dfs(now + 1, res * aa[now])
    else:
      if res < 0:
        dfs(now + 1, -((-res) // aa[now]))
      else:
        dfs(now + 1, res // aa[now])
    op[i] += 1


dfs(1, aa[0])
print(f'{mx}\n{mn}')
