import sys
a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()
result1 = []
result2 = 0

for i in range(0, 3):
  sum = 0
  n2 = int(b[i])
  for j in range(0, 3):
    n1 = int(a[j])
    sum += n1 * n2 * (10 ** (2 - j))
  result1.append(sum)
  result2 += sum * (10 ** (2 - i))

result1.reverse()

print('\n'.join(list(map(str, result1))))
print(result2)
