import sys
n = int(sys.stdin.readline())
nums = list(map(int, [sys.stdin.readline().strip() for _ in range(n)]))

def insertion_sort(arr):
  for i in range(1, len(arr)):
    j = i
    tmp = arr[i]
    while j > 0 and arr[j - 1] > tmp:
      arr[j] = arr[j - 1]
      j -= 1
    arr[j] = tmp

insertion_sort(nums)
print('\n'.join(map(str, nums)))