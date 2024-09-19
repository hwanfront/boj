import sys
n = int(sys.stdin.readline())
nums = list(map(int, [sys.stdin.readline().strip() for _ in range(n)]))

def selection_sort(arr):
  for i in range(len(arr) - 1):
    min_idx = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[min_idx]: 
        min_idx = j
    arr[min_idx], arr[i] = arr[i], arr[min_idx]

selection_sort(nums)
print('\n'.join(map(str, nums)))