def cvt_time_to_second(time):
    hour, minute, second = time.split(':')
    hour_second = int(hour) * 3600
    minute_second = int(minute) * 60
    second = int(second)

    return hour_second + minute_second + second


def cvt_second_to_time(second):
    hour = second // 3600
    second %= 3600
    minute = second // 60
    second %= 60

    return f"{hour:02}:{minute:02}:{second:02}"


def make_cumulative_lst(play_time_second, logs):
    cumulative_lst = [0] * (play_time_second + 1)

    for log in logs:
        start, end = log.split('-')
        start_second = cvt_time_to_second(start)
        end_second = cvt_time_to_second(end)

        cumulative_lst[start_second] += 1
        cumulative_lst[end_second] -= 1

    for idx in range(1, len(cumulative_lst)):
        cumulative_lst[idx] += cumulative_lst[idx - 1]

    return cumulative_lst


def search_adv_start_time(cumulative_lst, adv_time_second, play_time_second):
    start = 0
    adv_cnt = cnt = sum(cumulative_lst[:adv_time_second])
    adv_str = 0

    for end in range(adv_time_second, play_time_second):
        cnt -= cumulative_lst[start]
        start += 1
        cnt += cumulative_lst[end]

        if cnt > adv_cnt:
            adv_cnt = cnt
            adv_str = start

    return cvt_second_to_time(adv_str)


def solution(play_time, adv_time, logs):
    # cvt time to second
    play_time_second = cvt_time_to_second(play_time)
    adv_time_second = cvt_time_to_second(adv_time)

    cumulative_lst = make_cumulative_lst(play_time_second, logs)

    adv_start_time = search_adv_start_time(cumulative_lst, adv_time_second, play_time_second)

    return adv_start_time



if __name__ == "__main__":
    cases = [
        {'play_time': "02:03:55", 'adv_time': "00:14:15",
         'logs': ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
                  "01:37:44-02:02:30"]},
        {'play_time': "99:59:59", 'adv_time': "25:00:00",
         'logs': ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]},
        {'play_time': "50:00:00", 'adv_time': "50:00:00",
         'logs': ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]},
    ]

    for case in cases:
        print(solution(case['play_time'], case['adv_time'], case['logs']))