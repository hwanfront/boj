import sys
n = int(sys.stdin.readline())
nums = list(map(int, [sys.stdin.readline().strip() for _ in range(n)]))

def shaker_sort(arr):
  left = 0
  right = len(arr) - 1
  last = right
  while left < right:
    for i in range(right, left, -1):
      if arr[i - 1] > arr[i]:
        arr[i - 1], arr[i] = arr[i], arr[i - 1]
        last = i
    left = last

    for i in range(left, right):
      if arr[i] > arr[i + 1]:
        arr[i] , arr[i + 1] = arr[i + 1], arr[i] 
        last = i
    right = last

shaker_sort(nums)
print('\n'.join(map(str, nums)))