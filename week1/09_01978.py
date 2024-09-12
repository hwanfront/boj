import sys
n = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().strip().split()))
is_prime = [1 for _ in range(max(nums) + 1)]

is_prime[0] = is_prime[1] = 0

for i in range(2, max(nums) + 1):
  if is_prime[i] == 0: continue
  for j in range(i * 2, max(nums) + 1, i):
    is_prime[j] = 0

def check_prime(num):
  return is_prime[num] == 1

print(len([num for num in nums if check_prime(num)]))