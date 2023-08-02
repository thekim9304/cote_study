# https://school.programmers.co.kr/learn/courses/30/lessons/92335

def cvt_decimal_to_k_number(n, k):
    ret_base = ''

    while n > 0:
        n, mod = divmod(n, k)

        ret_base += str(mod)

    return ret_base[::-1]


def is_prime_number(x):
    if x == 2 or x == 3: return True
    if x % 2 == 0 or x < 2: return False

    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True


def solution(n, k):
    """
    변환된 수 안에 아래 조건에 맞는 소수(Prime number)가  몇 개인지
    0P0처럼 소수 양쪽에 0이 있는 경우
    P0처럼 소수 오른쪽에만 0이 있고 왼쪽에는 아무것도 없는 경우
    0P처럼 소수 왼쪽에만 0이 있고 오른쪽에는 아무것도 없는 경우
    P처럼 소수 양쪽에 아무것도 없는 경우
    단, P는 각 자릿수에 0을 포함하지 않는 소수입니다.
    예를 들어, 101은 P가 될 수 없습니다.
    :param n: 양의 정수
    :param k: n을 k 진수로 바꿈
    :return: 10진수로 바꿧을때 소수의 개수
    """
    answer = 0

    k_number = cvt_decimal_to_k_number(n, k)
    k_number_lst = k_number.split('0')

    for n in k_number_lst:
        if n and is_prime_number(int(n)):
            answer += 1

    return answer


if __name__ == '__main__':
    cases = [
        {'n': 437674, 'k': 3},
        {'n': 110011, 'k': 10}
    ]

    for case in cases:
        print(solution(case['n'], case['k']))