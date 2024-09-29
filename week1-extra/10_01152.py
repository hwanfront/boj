import sys
s = sys.stdin.readline().strip().split(' ')
if len(s) == 1 and s[0] == '':
  print(0)
else:
  print(len(s))