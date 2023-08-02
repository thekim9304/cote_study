# https://school.programmers.co.kr/learn/courses/30/lessons/72413

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

    dist = [INF for _ in range(n)]

    dist[src] = 0
    pq = [[0, src]]

    while pq:
        w, x = heappop(pq)

        if dist[x] < w:
            continue

        for nx, ncost in graph[x]:
            ncost += w

            if ncost < dist[nx]:
                dist[nx] = ncost

                heappush(pq, [ncost, nx])
    return dist[dst]


def solution(n, s, a, b, fares):
    """
    :param n: 지점의 개수
    :param s: 출발지점
    :param a: A의 도착지점
    :param b: B의 도착지점
    :param fares: 지점 사이의 예상 택시요금
    :return: 두 사람이 s에서 출발해서 각각의 도착 지점까지 택시를 타고 간다고 가정할 때, 최저 예상 택시 요금
    아예 합승하지 않고 각자 이동했을 때 더 낮으면 합승하지 않아도됨
    """
    preprocess(n, fares)

    cost = dijkstra(s, a) + dijkstra(s, b)

    for i in range(1, n+1):
        if s != i:
            cost = min(cost, dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b))

    return cost


if __name__ == "__main__":
    cases = [
        {'n': 6, 's': 4, 'a': 6, 'b': 2, 'fares': [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]},
        {'n': 7, 's': 3, 'a': 4, 'b': 1, 'fares': [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]},
        {'n': 6, 's': 4, 'a': 5, 'b': 6, 'fares': [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]},
    ]

    for case in cases:
        print(solution(case['n'], case['s'], case['a'], case['b'], case['fares']))