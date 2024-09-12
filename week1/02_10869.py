import sys
[a, b] = list(map(int, sys.stdin.readline().strip().split()))
print(f'{a+b}\n{a-b}\n{a*b}\n{int(a/b)}\n{a%b}')

# result = list([a+b, a-b, a*b, (int(a/b)), a%b])
# print('\n'.join(str(x) for x in result))
