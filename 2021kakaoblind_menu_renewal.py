'''
https://school.programmers.co.kr/learn/courses/30/lessons/72411
- 최소 2가지 이상의 요리로 구성된 코스 요리
- 코스별로 최소 2명 이상의 손님으로부터 가장 많이 주문된 단품메뉴 조합
'''
from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []

    for menu_cnt in course:
        combs = []

        for order in orders:
            combs.extend(list(combinations(sorted(order), menu_cnt)))

        combs_cnt = dict(Counter(combs))

        if combs_cnt:
            max_cnt = max([comb_cnt for comb_cnt in combs_cnt.values()])

        max_combs = list(filter(lambda x: x[1] == max_cnt, combs_cnt.items()))
        max_combs = list(filter(lambda x: x[1] > 1, max_combs))

        answer.extend([''.join(comb) for comb, cnt in max_combs])

    return sorted(answer)


if __name__ == '__main__':
    cases = [
        {'orders': ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], 'course': [2, 3, 4]},
        {'orders': ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], 'course': [2, 3, 5]},
        {'orders': ["XYZ", "XWY", "WXA"], 'course': [2, 3, 4]}
    ]

    for case in cases:
        print(solution(case['orders'], case['course']))