# ..? 이거 왜 통과함?
# https://www.acmicpc.net/source/84062664
import sys
n = int(sys.stdin.readline())
nums = list(map(int, [sys.stdin.readline().strip() for _ in range(n)]))

def shell_sort(arr):
  h = len(arr) // 2
  while h > 0:
    for i in range(h, len(arr)):
      j = i - h
      tmp = arr[i]
      while j >= 0 and arr[j] > tmp:
        arr[j + h] = arr[j]
        j -= h
      arr[j + h] = tmp
    h //= 2

shell_sort(nums)
print('\n'.join(map(str, nums)))