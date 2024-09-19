# import sys
# k = int(sys.stdin.readline().strip())
# result = []

# def dfs(now, color, cnt, graph, visited):

#   for next in graph[now]:


# for _ in range(k):
#   v, e = list(map(int, sys.stdin.readline().strip().split(' ')))
#   visited = [[False, False] for _ in range(v + 1)]
#   graph = [[] for _ in range(v + 1)]
  
#   for __ in range(e):
#     a, b = list(map(int, sys.stdin.readline().strip().split(' ')))
#     graph[a].append(b)
#     graph[b].append(a)
#   if dfs(1, 0, 0, graph, visited):
#     result.append('YES')
#   else:
#     result.append('NO')

# print('\n'.join(result))