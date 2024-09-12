# 각 원소를 1,000으로 나눈 나머지를 출력해야 하는ㄷ ㅔ 
# 입력으로 b가 1이고, 행렬에 1000이 들ㅇ오는 경우 초기값도 1000으로 ㅏㄴ누어ㅜ줘야햠

import sys
[n, b] = list(map(int, sys.stdin.readline().strip().split(' ')))
matrix = []
for i in range(0, n):
  matrix.append(list(map(int, sys.stdin.readline().strip().split(' '))))

obj = {}

init_matrix = matrix.copy()

for y in range(n):
  for x in range(n):
    init_matrix[y][x] %= 1000

obj[1] = init_matrix

def get_mul(matrix1, matrix2, y, x):
  sum = 0
  for i in range(n):
    sum += matrix1[y][i] * matrix2[i][x]
  return sum % 1000

def get_mul_matrix(matrix1, matrix2):
  mul_matrix = []
  for _ in range(0, n):
    mul_matrix.append([0] * n)
  for y in range(0, n):
    for x in range(0, n):
      mul_matrix[y][x] = get_mul(matrix1, matrix2, y, x)
  return mul_matrix
  
def go(now):
  if obj.get(now) == None:
    obj[now] = get_mul_matrix(go(now // 2), go(now - (now // 2)))
  return obj[now]

print('\n'.join(list(' '.join(list(map(str, e))) for e in go(b))))
