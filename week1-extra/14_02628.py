import sys
c, r = list(map(int, sys.stdin.readline().strip().split(' ')))
n = int(sys.stdin.readline().strip())
r_data = []
c_data = []

for _ in range(n):
  w, cost = list(map(int, sys.stdin.readline().strip().split()))
  if w == 0: 
    r_data.append(cost)
    continue
  c_data.append(cost)

r_data.sort()
c_data.sort()

r_max = 0
s = 0
for p in r_data:
  r_max = max(r_max, p - s)
  s = p
r_max = max(r_max, r - s)

c_max = 0
s = 0
for p in c_data:
  c_max = max(c_max, p - s)
  s = p
c_max = max(c_max, c - s)

if len(r_data) == 0:
  r_max = r

if len(c_data) == 0:
  c_max = c

print(r_max * c_max)