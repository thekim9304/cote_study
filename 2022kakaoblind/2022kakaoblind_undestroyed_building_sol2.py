def solution(board, skill):
    """
    :param board: 건물의 내구도
    :param skill: 공격 혹은 회복 스킬
    :return: 파괴되지 않은 건물의 개수
    """
    answer = 0
    temp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]

    for type, x1, y1, x2, y2, val in skill:
        temp[x1][y1] += val if type == 2 else -val
        temp[x1][y2 + 1] += -val if type == 2 else val
        temp[x2 + 1][y1] += -val if type == 2 else val
        temp[x2 + 1][y2 + 1] += val if type == 2 else -val

    for i in range(len(temp) - 1):
        for j in range(len(temp[0]) - 1):
            temp[i][j + 1] += temp[i][j]

    for j in range(len(temp[0]) - 1):
        for i in range(len(temp) - 1):
            temp[i + 1][j] += temp[i][j]

    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += temp[i][j]

            if board[i][j] > 0: answer += 1

    return answer


if __name__ == '__main__':
    cases = [
        {'board': [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], 'skill': 	[[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]},
        {'board': [[1,2,3],[4,5,6],[7,8,9]], 'skill': [[1,1,1,2,2,4],[1,0,0,1,1,2],[2,2,0,2,0,100]]}
    ]

    for case in cases:
        print(solution(case['board'], case['skill']))