def solution(id_list, report, k):
    """
    :param id_list: 이용자의 ID가 담긴 문자열 배열
    :param report: 각 이용자가 신고한 이용자의 ID 정보가 담긴 문자열 배열
    :param k: 정지 기준이 되는 신고 횟수
    :return: 각 유저별로 처리 결과 메일을 받은 횟수를 배열에 담아 리턴
    """
    answer = []

    id_report_dict = {user_id: [] for user_id in id_list}
    reported_dict = {user_id: 0 for user_id in id_list}
    for rep in report:
        request_id, target_id = rep.split()

        if target_id not in id_report_dict[request_id]:
            id_report_dict[request_id].append(target_id)
            reported_dict[target_id] += 1

    cut_id_lst = list(filter(lambda x: x[1] >= k, reported_dict.items()))
    cut_id_lst = set([x[0] for x in cut_id_lst])

    for user_id, report_lst in id_report_dict.items():
        answer.append(len(set(report_lst).intersection(cut_id_lst)))

    return answer


if __name__ == '__main__':
    cases = [
        {'id_list': ["muzi", "frodo", "apeach", "neo"], 'report': ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 'k': 2},
        {'id_list': ["con", "ryan"], 'report': ["ryan con", "ryan con", "ryan con", "ryan con"], 'k': 3}
    ]

    for case in cases:
        print(solution(case['id_list'], case['report'], case['k']))