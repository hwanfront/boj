import sys

def merge(l, r):
  result = []
  li = ri = 0

  while li < len(l) and ri < len(r):
    if l[li] < r[ri]:
      result.append(l[li])
      li += 1
    else:
      result.append(r[ri])
      ri += 1
  
  result.extend(l[li:])
  result.extend(r[ri:])

  return result

def merge_sort(arr):
  if len(arr) == 1:
    return arr
  
  mid = len(arr) // 2
  l = merge_sort(arr[:mid])
  r = merge_sort(arr[mid:])
  return merge(l, r)

arr = list(map(int, sys.stdin.readline().strip().split(' ')))
print()
print('prev: ', arr)
arr = merge_sort(arr)
print('sorted: ', arr)