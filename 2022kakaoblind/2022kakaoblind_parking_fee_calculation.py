# https://school.programmers.co.kr/learn/courses/30/lessons/92341?language=python3

from math import ceil


def cvt_time_to_minute(time):
    hour, minute = time.split(":")

    hour_minute = int(hour) * 60

    return hour_minute + int(minute)


def solution(fees, records):
    """
    :param fees: 요금표 [기본 시간(분), 기본 요금(원), 단위 시간(분), 단위 요금(원)]
    :param records: 입/출차 기록
    :return: 차량 번호가 작은 자동차부터 청구할 주차 요금
    """
    answer = []

    base_minute, base_cost, unit_minute, unit_cost = fees

    log_dict = {}
    for record in records:
        time, number, action = record.split()

        time_minute = cvt_time_to_minute(time)

        if number in log_dict:
            log_dict[number][action].append(time_minute)
        else:
            log_dict[number] = {'IN': [time_minute], 'OUT': []}

    log_lst = sorted(log_dict.items(), key = lambda x: x[0])

    for number, logs in log_lst:
        acommul_minute = 0
        for in_minute, out_minute in zip(logs['IN'], logs['OUT']):
            acommul_minute += (out_minute - in_minute)

        if len(logs['IN']) != len(logs['OUT']):
            acommul_minute += (cvt_time_to_minute("23:59") - logs['IN'][-1])

        total_cost = base_cost
        if acommul_minute > base_minute:
            total_cost = base_cost + ceil((acommul_minute - base_minute) / unit_minute) * unit_cost

        answer.append(total_cost)

    return answer


if __name__ == "__main__":
    cases = [
        {'fees': [180, 5000, 10, 600],
         'records': ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]},
        {'fees': [120, 0, 60, 591],
         'records': ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]},
        {'fees': [1, 461, 1, 10], 'records': ["00:00 1234 IN"]},
    ]

    for case in cases:
        print(solution(case['fees'], case['records']))