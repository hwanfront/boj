
import sys
[n, b] = list(map(int, sys.stdin.readline().strip().split(' ')))
matrix = []
for i in range(0, n):
  matrix.append(list(map(int, sys.stdin.readline().strip().split(' '))))

init_matrix = matrix.copy()

for y in range(n):
  for x in range(n):
    init_matrix[y][x] %= 1000

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
  
def go(matrix, now):
  if now == 1:
    return init_matrix
  value = go(matrix, now // 2)
  value = get_mul_matrix(value, value)
  if now % 2 == 1:
      value = get_mul_matrix(value, matrix)
  return value

print('\n'.join(list(' '.join(list(map(str, e))) for e in go(init_matrix, b))))
