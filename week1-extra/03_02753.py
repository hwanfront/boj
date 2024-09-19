import sys
n = int(sys.stdin.readline().strip())
def get_yn(n):
  if n % 400 == 0:
    return 1
  if n % 100 == 0:
    return 0
  if n % 4 == 0:
    return 1
  return 0

print(get_yn(n))