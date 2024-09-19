import sys
n = int(sys.stdin.readline())
nums = list(map(int, [sys.stdin.readline().strip() for _ in range(n)]))

def bubble_sort(arr):
  n = len(arr)
  for i in range(n - 1):
    for j in range(n - 1, i, -1):
      if arr[j - 1] <= arr[j]:
        continue
      arr[j - 1], arr[j] = arr[j], arr[j - 1]

bubble_sort(nums)
print('\n'.join(map(str, nums)))