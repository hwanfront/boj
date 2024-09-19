# 복잡도
## 시간복잡도
시간복잡도 표기법에는 최상의 실행시간을 나타내는 빅 오메가, 평균 실행시간을 나타내는 빅 세타가 있습니다. 알고리즘의 효율을 나타낼때 사용하며 최악의 실행 시간을 표기합니다. 
### big-O notation
상수항과 계수는 무시하고 최고차항만을 표기합니다. 예를들어 계산했을 때 (2n^2 + 3) 가 나온다면 O(n^2)라고 표기합니다. 실행 속도는 `O(1)` `O(logn)` `O(n)` `O(nlogn)` `O(n^2)` `O(2^n)` 순서입니다. 추가로 알고리즘 문제를 풀 때 1억회 연산을 수행시간 1초로 기준을 잡고 계산을 한다네요?
- `O(1)`: push pop 
- `O(logn)`: `이진트리` 
- `O(n)`: for 문 
- `O(nlogn)`: `quick sort` `merge sort` `heap Sort`
- `O(n^2)`: 이중 for 문, `insertion sort` `bubble sort` `selection sort`
- `O(2^n)`: 피보나치 수열

## 공간복잡도
얼마나 많은 메모리를 사용하는지 나타냅니다. 고정공간은 코드 저장공간이나 단순한 변수 상수 등 입출력과 관계없는 부분을 의미하고, 나머지 동적으로 필요한 공간을 가변공간이라고 합니다. 
```
Common Data Structure Operations
Data Structure	Time Complexity	Space Complexity
Average	Worst	Worst
Access	Search	Insertion	Deletion	Access	Search	Insertion	Deletion	
Array	Θ(1)	Θ(n)	Θ(n)	Θ(n)	O(1)	O(n)	O(n)	O(n)	O(n)
Stack	Θ(n)	Θ(n)	Θ(1)	Θ(1)	O(n)	O(n)	O(1)	O(1)	O(n)
Queue	Θ(n)	Θ(n)	Θ(1)	Θ(1)	O(n)	O(n)	O(1)	O(1)	O(n)
Singly-Linked List	Θ(n)	Θ(n)	Θ(1)	Θ(1)	O(n)	O(n)	O(1)	O(1)	O(n)
Doubly-Linked List	Θ(n)	Θ(n)	Θ(1)	Θ(1)	O(n)	O(n)	O(1)	O(1)	O(n)
Skip List	Θ(log(n))	Θ(log(n))	Θ(log(n))	Θ(log(n))	O(n)	O(n)	O(n)	O(n)	O(n log(n))
Hash Table	N/A	Θ(1)	Θ(1)	Θ(1)	N/A	O(n)	O(n)	O(n)	O(n)
Binary Search Tree	Θ(log(n))	Θ(log(n))	Θ(log(n))	Θ(log(n))	O(n)	O(n)	O(n)	O(n)	O(n)
Cartesian Tree	N/A	Θ(log(n))	Θ(log(n))	Θ(log(n))	N/A	O(n)	O(n)	O(n)	O(n)
B-Tree	Θ(log(n))	Θ(log(n))	Θ(log(n))	Θ(log(n))	O(log(n))	O(log(n))	O(log(n))	O(log(n))	O(n)
Red-Black Tree	Θ(log(n))	Θ(log(n))	Θ(log(n))	Θ(log(n))	O(log(n))	O(log(n))	O(log(n))	O(log(n))	O(n)
Splay Tree	N/A	Θ(log(n))	Θ(log(n))	Θ(log(n))	N/A	O(log(n))	O(log(n))	O(log(n))	O(n)
AVL Tree	Θ(log(n))	Θ(log(n))	Θ(log(n))	Θ(log(n))	O(log(n))	O(log(n))	O(log(n))	O(log(n))	O(n)
KD Tree	Θ(log(n))	Θ(log(n))	Θ(log(n))	Θ(log(n))	O(n)	O(n)	O(n)	O(n)	O(n)
```