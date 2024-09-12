import sys

def get_fact(n: int) -> int:
  if n == 0:
    return 1
  return n * get_fact(n - 1)

n = int(sys.stdin.readline().strip())

print(get_fact(n))