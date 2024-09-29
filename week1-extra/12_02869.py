import sys
a, b, v = list(map(int, sys.stdin.readline().strip().split(' ')))
if (v - a) % (a - b) == 0:
  print((v - b) // (a - b))
else:
  print((v - b) // (a - b) + 1)


