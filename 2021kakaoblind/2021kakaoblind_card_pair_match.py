def solution(board, r, c):
    """
    :param board: 4x4 크기의 2차원 배열 (0이상 6이하인 자연수)
        - 0 _ 카드가 제거된 빈 칸
        - 1 ~ 6 _ 2개씩 들어있으며 같은 숫자는 같은 그림의 카드를 의미
    :param r: 커서의 최소 세로(행) 위치
        - 0 ~ 3 정수
    :param c: 커서의 최초 가로(열) 위치
        - 0 ~ 3 정수
    :return: 모든 카드를 제거하기 위한 키 조작 횟수의 최솟값
    """
    answer = 0
    return answer


if __name__ == '__main__':
    cases = [
        {'board': [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 'r': 1, 'c': 0},
        {'board': [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 'r': 0, 'c': 1}
    ]

    for case in cases[:1]:
        print(solution(case['board'], case['r'], case['c']))
