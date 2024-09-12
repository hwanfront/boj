import sys
ts = int(sys.stdin.readline().strip())
if ts >= 90: 
  print('A')
elif ts >= 80: 
  print('B')
elif ts >= 70: 
  print('C')
elif ts >= 60: 
  print('D')
else: 
  print('F')
