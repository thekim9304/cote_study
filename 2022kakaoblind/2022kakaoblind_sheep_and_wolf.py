# https://school.programmers.co.kr/learn/courses/30/lessons/92344

def solution(info, edges):
    """
    :param info: 양 또는 늑대에 대한 정보가 담긴 배열
    :param edges: 2진 트리의 각 노드들의 연결 관계를 담은 2차원 배열
    :return: 모을 수 있는 양의 최대 수
    """
    answer = 0

    visited = [0] * len(info)
    answer = []

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = 1
                if info[c] == 0:
                    dfs(sheep + 1, wolf)
                else:
                    dfs(sheep, wolf + 1)
                visited[c] = 0

    # 루트 노드부터 시작
    visited[0] = 1
    dfs(1, 0)

    return max(answer)

    return answer


if __name__ == "__main__":
    cases = {
        {'info': [0,0,1,1,1,0,1,0,1,0,1,1], 'edges': [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]},
        {'info': [0,1,0,1,1,0,1,0,0,1,0], 'edges': [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]}
    }