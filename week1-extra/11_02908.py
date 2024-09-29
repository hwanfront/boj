import sys
a, b = sys.stdin.readline().strip().split(' ')

aa = int(a[2] + a[1] + a[0])
bb = int(b[2] + b[1] + b[0])

if aa > bb:
  print(aa)
else:
  print(bb)