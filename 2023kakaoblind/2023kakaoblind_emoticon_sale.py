from itertools import product

def solution(users, emoticons):
    """
    - n명의 카카오톡 사용자들에게 이모티콘 m개를 할인하여 판매
    - 할인율은 10%, 20%, 30%, 40% 중 하나로 설정됨
    - 기준
        - 일정 비율 이상 할인하는 이모티콘을 모두 구매
        - 이모티콘 구매 비용의 합이 일정 가격 이상이 된다면, 이모티콘 구매 취소 -> 프러스 가입
    :param users: 유저의 구매 기준 배열
    :param emoticons: 이모티콘의 정가
    :return: [행사 목적을 최대한 달성했을 때의 이모티콘 플러스 서비스 가입 수, 이모티콘 매출액]
    """
    answer = []

    discount_rate_lst = [10, 20, 30, 40]

    num_emoticon = len(emoticons)

    discount_rate_perm = list(product(discount_rate_lst, repeat=num_emoticon))


    res_join_cnt = 0
    res_total_price = 0
    for discount_rate in discount_rate_perm:
        discount_price = [[discount, price * (1 - (discount * 0.01))] for price, discount in zip(emoticons, discount_rate)]

        join_cnt = 0
        total_price = 0

        for pick_discount, max_price in users:
            remain_emoticon = list(filter(lambda x: x[0] >= pick_discount, discount_price))

            remain_emoticon_price = [remain_em[1] for remain_em in remain_emoticon]

            buy_price = sum(remain_emoticon_price)

            if buy_price >= max_price:
                join_cnt += 1
            else:
                total_price += buy_price

        if join_cnt > res_join_cnt:
            res_join_cnt = join_cnt
            res_total_price = total_price
        elif join_cnt == res_join_cnt:
            if total_price > res_total_price:
                res_join_cnt = join_cnt
                res_total_price = total_price

    answer = [res_join_cnt, int(res_total_price)]

    return answer


if __name__ == '__main__':
    cases = [
        {'users': [[40, 10000], [25, 10000]], 'emoticons': 	[7000, 9000]},
        {'users': [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], 'emoticons': [1300, 1500, 1600, 4900]},
    ]

    for case in cases[1:]:
        print(solution(case['users'], case['emoticons']))