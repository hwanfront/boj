import sys
n = int(sys.stdin.readline().strip())
result = 99
if n < 100:
  print(n)
  exit()
if n > 110:
  num = (n // 100) - 1
  result += num * 5
  if n != 1000:
    tmp = n // 100
    for i in range(1, 5):
      tp1 = tmp - i
      tp2 = tmp - (i * 2)
      tm1 = tmp + i
      tm2 = tmp + (i * 2)
      if tp1 >= 0 and tp2 >= 0 and tp1 < 10 and tp2 < 10:
        if tmp * 100 + tp1 * 10 + tp2 <= n:
          result += 1
      if tm1 >= 0 and tm2 >= 0 and tm1 < 10 and tm2 < 10:
        if tmp * 100 + tm1 * 10 + tm2 <= n:
          result += 1
    if tmp * 100 + tmp * 10 + tmp <= n:
      result += 1

print(result)
