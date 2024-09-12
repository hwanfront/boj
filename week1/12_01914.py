import sys
result = []
def hanoi(cnt: int, start, to, tmp):
  if cnt == 1:
    # print(f'[{cnt}]', start, tmp, to)
    result.append(f'{start} {to}')
    return
  hanoi(cnt - 1, start, tmp, to)
  # print(f'[{cnt}]', start, tmp, to)
  result.append(f'{start} {to}')
  hanoi(cnt - 1, tmp, to, start)

n = int(sys.stdin.readline().strip())

def calc_hanoi_cnt(cnt):
  sum = 0
  for i in range(cnt):
    sum += 2 ** i
  return sum

if n > 20:
  print(calc_hanoi_cnt(n))
else:
  hanoi(n, '1', '3', '2')
  print(len(result))
  print(*result, sep='\n')