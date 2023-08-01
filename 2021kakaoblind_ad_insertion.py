# https://school.programmers.co.kr/learn/courses/30/lessons/72414

def cvt_time_str_to_second(time_str):
    hour, minute, second = time_str.split(":")
    hour = int(hour) * 3600
    minute = int(minute) * 60
    second = int(second)

    return hour + minute + second


def cvt_second_to_time_str(second):
    hour = second // 3600
    second %= 3600
    minute = second // 60
    second %= 60
    second = second

    return f"{hour:02}:{minute:02}:{second:02}"


def set_sec_arr(logs):
    global sec_arr, play_time_second

    for log in logs:
        start_str, end_str = log.split('-')
        start_second = cvt_time_str_to_second(start_str)
        end_second = cvt_time_str_to_second(end_str)

        sec_arr[start_second] += 1
        sec_arr[end_second] -= 1

    # 누적 합
    for idx in range(1, play_time_second):
        sec_arr[idx] += sec_arr[idx - 1]


def search_start_time(play_time_sec, adv_time_sec):
    global sec_arr

    start = 0
    ans_cnt = cnt = sum(sec_arr[:adv_time_sec])
    ans_str = 0

    for end in range(adv_time_sec, play_time_sec):
        cnt -= sec_arr[start]
        start += 1
        cnt += sec_arr[end]

        if ans_cnt < cnt:
            ans_cnt = cnt
            ans_str = start

    return cvt_second_to_time_str(ans_str)


def solution(play_time, adv_time, logs):
    """
    :param play_time: 재생시간 길이 (HH:MM:SS)
    :param adv_time: 공익광고의 재생시간 길이 (HH:MM:SS)
    :param logs: 시청자들이 해당 동영상을 재생했던 구간 정보 (H1:M1:S1-H2:M2:S2)
    :return: 공익광고가 들어갈 시작 시간
        - 시청자들의 누적 재생시간이 가장 많이 나오는 곳에 공익광고 삽입
        - 누적 재생시간이 가장 많은 곳이 여러 곳이라면 가장 빠른 시작 시간을 return
    """
    global sec_arr, play_time_second, adv_time_second

    play_time_second = cvt_time_str_to_second(play_time) + 1
    adv_time_second = cvt_time_str_to_second(adv_time)

    sec_arr = [0] * play_time_second

    set_sec_arr(logs)

    answer = search_start_time(play_time_second, adv_time_second)

    return answer


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