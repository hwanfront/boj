import sys
from collections import deque
n = int(sys.stdin.readline().strip())
card = deque(list(range(1, n + 1)))
_is = False

while len(card) > 1:
  _is = not _is
  if _is:
    card.popleft()
  else:
    card.append(card.popleft())

print(card[0])