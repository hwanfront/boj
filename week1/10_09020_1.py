import math
import sys

def is_prime(n):
  if n <= 1: return False
  for i in range(2, int(math.sqrt(n) + 1)):
    if n % i == 0: 
      return False
  return True

def get_gbp(n: int) -> str:
  for i in reversed(range(2, int(n / 2) + 1)):
    if is_prime(i) and is_prime(n - i):
      return f'{i} {n - i}'

t = int(sys.stdin.readline())
nn = list(map(int, [sys.stdin.readline().strip() for _ in range(t)]))
result = ''

for n in nn:
  result += get_gbp(n) + '\n'

print(result.strip())
