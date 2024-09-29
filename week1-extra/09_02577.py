import sys
a = int(sys.stdin.readline().strip())
b = int(sys.stdin.readline().strip())
c = int(sys.stdin.readline().strip())
cnt = [0] * 10
num = str(a * b * c)
for s in num:
  cnt[int(s)] += 1
print('\n'.join(map(str, cnt)))