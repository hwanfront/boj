import sys
n = int(sys.stdin.readline())
words = list(set([sys.stdin.readline().strip() for _ in range(n)]))
words.sort()
print('\n'.join(sorted(words, key=len)))