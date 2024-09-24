import sys
sys.setrecursionlimit(10**5)
nums = []
result = []

while True:  
  try:
    nums.append(int(sys.stdin.readline()))
  except:
    break

stack = []
arr = []

for num in nums:
  if not stack:
    stack.append(num)
    continue
  while stack and stack[-1] < num:
    arr.append(stack.pop())
  stack.append(num)

while stack:
  arr.append(stack.pop())

def go(pl, pr, il, ir, pre_order, in_order):
  if pl > pr:
    return
  if pl == pr:
    result.append(pre_order[pl])
    return
  root = pre_order[pl]
  idx = None
  for i in range(il, ir + 1):
    if in_order[i] == root:
      idx = i - il
  go(pl + 1, pl + idx, il, il + idx - 1, pre_order, in_order)
  go(pl + 1 + idx, pr, il + idx + 1, ir, pre_order, in_order)
  result.append(pre_order[pl])

go(0, len(nums) - 1, 0, len(nums) - 1, nums, arr)

print('\n'.join(map(str, result)))