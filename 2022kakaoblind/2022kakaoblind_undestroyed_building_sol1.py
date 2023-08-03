import numpy as np

def solution(board, skill):
    """
    :param board: 건물의 내구도
    :param skill: 공격 혹은 회복 스킬
    :return: 파괴되지 않은 건물의 개수
    """
    answer = 0

    board = np.array(board)

    for type, x1, y1, x2, y2, val in skill:
        if type == 1:
            board[x1: x2 + 1, y1: y2 + 1] -= val
        else:
            board[x1: x2 + 1, y1: y2 + 1] += val

    answer = int(np.sum(board > 0))

    return answer


if __name__ == '__main__':
    cases = [
        {'board': [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], 'skill': 	[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]},
        {'board': [[1,2,3],[4,5,6],[7,8,9]], 'skill': [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]}
    ]

    for case in cases:
        print(solution(case['board'], case['skill']))