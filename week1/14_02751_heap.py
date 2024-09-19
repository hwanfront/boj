import sys
n = int(sys.stdin.readline())
nums = list(map(int, [sys.stdin.readline().strip() for _ in range(n)]))

def heapify(arr, n, i):
  root = i
  left = 2 * i + 1
  right = 2 * i + 2

  if left < n and arr[root] < arr[left]:
    root = left
  
  if right < n and arr[root] < arr[right]:
    root = right
  
  if root == i:
    return
  
  arr[i], arr[root] = arr[root], arr[i]
  heapify(arr, n, root)

def heap_sort(arr):
  for i in range(len(arr) // 2 - 1, -1, -1):
    heapify(arr, len(arr), i)
  
  for i in range(len(arr) - 1, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    heapify(arr, i, 0)
    
heap_sort(nums)
print('\n'.join(map(str, nums)))