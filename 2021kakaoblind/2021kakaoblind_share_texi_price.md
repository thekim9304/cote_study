우선순위 큐
-
- 일반적인 큐(Queue)는 먼저 집어넣은 데이터가 먼저 나오는 FIFO(First In First Out) 구조
- 우선순위 큐(Priority Queue)는 들어간 순서에 상관 없이 우선순위가 높은 데이터가 먼저 나오는 것을 말함
- 우선순위 큐 속성
  1. 모든 항목에는 우선순위가 있음
  2. 우선 순위가 높은 요소는 우선 순위가 낮은 요소보다 먼저 queue에서 제외됨
  3. 두 요소의 우선 순위가 같으면 queue의 순서에 따라 제외됨

다익스트라 알고리즘
-
- 그래프에서 한 정점(노드)에서 다른 정점까지의 최단 경로를 구하는 알고리즘
```python
from heapq import heappop, heappush

INF = int(1e9)
graph = [[]]


def preprocess(n, fares):
    global graph
    graph = [[] for i in range(n+1)]

    for fare in fares:
        src, dst, cost = fare[0], fare[1], fare[2]
        graph[src].append([dst, cost])
        graph[dst].append([src, cost])


def dijkstra(src, dst):
    global graph
    n = len(graph)
    # 거리 저장 배열
    dist = [INF for _ in range(n)]
    # 첫 정점의 거리는 0
    dist[src] = 0
    # 우선순위 큐에 (거리 0, 첫 정점)만 먼저 넣는다.
    pq = [[0,src]]

    while pq:
        w, x = heappop(pq)

        # 거리배열에 저장된 값이 더 큰 경우에만 업데이트
        if dist[x] < w:
            continue

        for item in graph[x]:
            nx, ncost = item[0], item[1]
            ncost += w
            # 현재 노드까지 거리 + 해당 노드로부터 연결된 다른 노드로 거리가 더 작을 때 업데이트
            if ncost < dist[nx]:
                dist[nx] = ncost
                # 우선순위큐에 넣어줌
                heappush(pq, [ncost, nx])
    return dist[dst]
```