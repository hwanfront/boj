import sys

def get_is_prime(to: int) -> list[bool]:
  is_prime = [True for _ in range(to + 1)]

  is_prime[0] = is_prime[1] = False

  for i in range(2, to + 1):
    if not is_prime[i]: continue
    for j in range(i * 2, to + 1, i):
      is_prime[j] = False

  return is_prime

def get_gbp(n: int, is_prime: list[bool]) -> str:
  for i in reversed(range(2, int(n / 2) + 1)):
    if is_prime[i] and is_prime[n - i]:
      return f'{i} {n - i}'

t = int(sys.stdin.readline())
nn = list(map(int, [sys.stdin.readline().strip() for _ in range(t)]))
is_prime = get_is_prime(max(nn) + 1)
result = ''

for n in nn:
  result += get_gbp(n, is_prime) + '\n'

print(result.strip())
