# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def cvt_binary_lst(arr, n):
    lst = [[int(_a) for _a in format(a, 'b')] for a in arr]

    return [([0] * (n - len(_a))) + _a for _a in lst]


def solution(n, arr1, arr2):
    answer = []

    arr1 = cvt_binary_lst(arr1, n)
    arr2 = cvt_binary_lst(arr2, n)

    for ar1, ar2 in zip(arr1, arr2):
        sum_lst = [x + y for x, y in zip(ar1, ar2)]

        res_lst = ['#' if val >= 1 else ' ' for val in sum_lst]

        res_str = ''.join(res_lst)

        answer.append(res_str)

    return answer


if __name__ == '__main__':
    cases = [
        {'n': 5, 'arr1': [9, 20, 28, 18, 11], 'arr2': [30, 1, 21, 17, 28]},
        {'n': 6, 'arr1': [46, 33, 33, 22, 31, 50], 'arr2': [27, 56, 19, 14, 14, 10]}
    ]

    for case in cases:
        print(solution(case['n'], case['arr1'], case['arr2']))