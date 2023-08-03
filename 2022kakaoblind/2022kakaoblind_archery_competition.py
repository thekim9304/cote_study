# https://school.programmers.co.kr/learn/courses/30/lessons/92342

from itertools import combinations_with_replacement


def solution(n, info):
    answer = [-1]
    max_gap = -1

    for combi in combinations_with_replacement(range(11), n):
        info2 = [0] * 11

        for i in combi:
            info2[10 - i] += 1

        apeach, lion = 0, 0
        for idx in range(11):
            if info[idx] == info2[idx] == 0:
                continue
            elif info[idx] >= info2[idx]:
                apeach += 10 - idx
            else:
                lion += 10 - idx

        if lion > apeach:
            gap = lion - apeach
            if gap > max_gap:
                max_gap = gap
                answer = info2
    return answer


if __name__ == '__main__':
    cases = {
        'n': 5, 'info': [2,1,1,1,0,0,0,0,0,0,0],
        'n': 1, 'info': [1,0,0,0,0,0,0,0,0,0,0],
        'n': 9, 'info': [0,0,1,2,0,1,1,1,1,1,1],
        'n': 10, 'info': [0,0,0,0,0,0,0,0,3,4,3]
    }