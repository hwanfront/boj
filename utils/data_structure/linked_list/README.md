# Linked List
각 노드가 데이터와 다음 노드의 포인터를 가지는 자료구조입니다. 노드들이 메모리의 임의의 위치에 저장되어 Array 처럼 낭비되는 메모리가 발생하지는 않습니다. 포인터를 위한 메모리가 요구됩니다. 데이터를 탐색하는 경우 순차적으로 탐색해야 하기 때문에 시간이 오래 걸립니다.
## Linked List 의 특징
- 동적인 크기를 갖습니다.
- 논리적 저장 순서와 물리적 저장 순서가 일치하지 않습니다.
- 메모리가 연속적이지 않으므로 `Cache Hit Ratio`가 낮습니다.
- 주로 삽입과 삭제가 주가 되는 경우 유용합니다.
## Complexity
### Time Complexity
- access: Θ(n), O(n)
- search: Θ(n), O(n)
- add: Θ(1), O(1)
- remove: Θ(1), O(1)
### Space Complexity
- O(n)