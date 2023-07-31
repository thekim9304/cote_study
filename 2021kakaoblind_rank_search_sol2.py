'''
https://school.programmers.co.kr/learn/courses/30/lessons/72412
- Binary Search 사용
    - lower bound
'''
from itertools import combinations
from collections import defaultdict

def lower_bound(nums, target):
    start, end = 0, len(nums)

    while start < end:  # left와 right가 만나는 지점이 target값 이상이 처음 나오는 위치
        mid = start + (end - start) // 2

        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid

    return end


def solution2(info, query):
    '''
    이분 탐색
    정확성 통과
    효율성 통과
    '''
    answer = []
    info_dict = defaultdict(list)
    for info_str in info:
        info_lst = info_str.split()
        condition = info_lst[:-1]
        score = int(info_lst[-1])

        for i in range(5):
            cases = list(combinations([0, 1, 2, 3], i))

            for case in cases:
                tmp = condition.copy()
                for idx in case:
                    tmp[idx] = '-'
                key = ''.join(tmp)
                info_dict[key].append(score)

    for value in info_dict.values():
        value.sort()

    for q in query:
        q = q.replace(" and ", " ")
        q_lst = q.split()

        target_key = ''.join(q_lst[:-1])
        target_score = int(q_lst[-1])

        count = 0
        if target_key in info_dict:
            target_list = info_dict[target_key]
            idx = lower_bound(target_list, target_score)
            count = len(target_list) - idx

        answer.append(count)

    return answer


if __name__ == '__main__':
    cases = [
        {'info': ["java backend junior pizza 150", "python frontend senior chicken 210",
                  "python frontend senior chicken 150", "cpp backend senior pizza 260",
                  "java backend junior chicken 80", "python backend senior chicken 50"],
         'query': ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
                   "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
                   "- and - and - and chicken 100", "- and - and - and - 150"]}
    ]

    for case in cases:
        print(solution2(case['info'], case['query']))