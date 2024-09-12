import sys
n = int(sys.stdin.readline().strip())
result = ''

def mul(n: int, i: int) -> str:
  return f'{n} * {i} = {n * i}'

result += mul(n, 1)

for i in range(2, 10):
  result += f'\n{mul(n, i)}'

print(result)