import sys
n = int(sys.stdin.readline().strip())
square = []
wCnt = 0
bCnt = 0
for _ in range(n):
  square.append(sys.stdin.readline().strip().split(' '))

def make(y, x, size):
  global wCnt, bCnt
  color = square[y][x]
  if size == 1:
    if color == '1': bCnt += 1
    else: wCnt += 1
    return

  _is = True
  for i in range(y, y + size):
    for j in range(x, x + size):
      if square[i][j] != color:
        _is = False
        break
      
  if _is:
    if color == '1': bCnt += 1
    else: wCnt += 1
    return
  
  make(y, x, size // 2)
  make(y + size // 2, x, size // 2)
  make(y, x + size // 2, size // 2)
  make(y + size // 2, x + size // 2, size // 2)
    
make(0, 0, n)

print(f'{(wCnt)}\n{(bCnt)}')