import sys
from collections import deque

def check(y, x):
  return 0 <= y and y < n and 0 <= x and x < n

def turn(sd, c):
  if c == 'D':
    if sd == 3:
      return 0
    return sd + 1
  if sd == 0:
    return 3
  return sd - 1

n = int(sys.stdin.readline().strip())
k = int(sys.stdin.readline().strip())
applsPos = [list(map(int, sys.stdin.readline().strip().split(' '))) for _ in range(0, k)]
l = int(sys.stdin.readline().strip())
infos = [sys.stdin.readline().strip().split(' ') for _ in range(0, l)]

board = [[0] * n for _ in range(0, n)]
d = [[0, 1],[1, 0],[0, -1],[-1, 0]]

snake = deque()
sd = 0
result = 0
prev = 0

for [y, x] in applsPos:
  board[y - 1][x - 1] = -1

snake.append([0, 0])
board[0][0] = 1

gameover = False
for [to, c] in infos:
  for i in range(prev, int(to)):
    [y, x] = snake[0] # head
    [dy, dx] = d[sd]
    [ny, nx] = [y + dy, x + dx]
    result += 1
    if not check(ny, nx) or board[ny][nx] == 1: 
      gameover = True
      break
    snake.appendleft([ny, nx])
    if board[ny][nx] != -1:
      tail = snake.pop()
      board[tail[0]][tail[1]] = 0
    board[ny][nx] = 1
  
  if gameover == True:
    break
  sd = turn(sd, c)
  prev = int(to)

if gameover == True:
  print(result)
else:
  while 1:
    [y, x] = snake[0] # head
    [dy, dx] = d[sd]
    [ny, nx] = [y + dy, x + dx]
    result += 1
    if not check(ny, nx) or board[ny][nx] == 1: 
      gameover = True
      break
    snake.appendleft([ny, nx])
    if board[ny][nx] != -1:
      tail = snake.pop()
      board[tail[0]][tail[1]] = 0
    board[ny][nx] = 1

  print(result)
