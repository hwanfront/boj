import sys
n = int(sys.stdin.readline())
nums = list(map(int, [sys.stdin.readline().strip() for _ in range(n)]))
nums.sort()
print('\n'.join(map(str, nums)))