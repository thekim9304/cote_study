def(Depth-First Search)
-
- 깊이 우선 탐색
- **스택 자료구조**를 이용
![](https://blog.kakaocdn.net/dn/cclCgg/btrcojV3msS/Tv0YKd4DMEA8kM927xCCfK/img.gif)
```python
def dfs_with_adj_list(graph, root):
    visited = []
    stack = [root]
    
    while stack:
        n = stack.pop()
        
        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)
    
    return visited
```

bfs(Breadth-First Search)
-
- 너비 우선 탐색
- 그래프에서 **가까운 노드부터 우선적으로 탐색**하는 알고리즘
- **큐 자료구조**를 이용
  1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
  2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
  3. 더 이상 2번의 과정을 수행할 수 없을 때까지 반복
![](https://blog.kakaocdn.net/dn/domqAK/btrcxJ6zUpY/zYqGKW7ECBEofu9LqK6ic0/img.gif)
```python
from collections import deque

def bfs_with_adj_list(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()

        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)

    return visited
```