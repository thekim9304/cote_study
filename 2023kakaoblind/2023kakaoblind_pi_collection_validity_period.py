from datetime import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    """
    - 1~n번으로 분류되는 개인정보 n개가 있음
    - 약관 종류는 여러 가지, 약관마다 개인정보 보호 유호기간 정해져있음
    - 유효기간 전까지 보관 가능하며, 지나면 반드시 파기해야 함
    - 모든 달은 28일 까지
    -
    :param today: 오늘 날짜
    :param terms: 약관의 유효기간을 담은 1차원 문자열 배열
    :param privacies: 개인정보의 정보를 담은 1차원 문자열 배열
    :return: 파기해야 할 개인정보의 번호를 오름차순으로 리턴
    """
    answer = []

    today = datetime.strptime(today, "%Y.%m.%d")

    term_dict = {}
    for term in terms:
        agree_type, period = term.split()
        term_dict[agree_type] = int(period)

    for i, privacy in enumerate(privacies):
        date, agree_type = privacy.split()

        date_expiration = datetime.strptime(date, "%Y.%m.%d") + relativedelta(months=term_dict[agree_type])

        if date_expiration <= today:
            answer.append(i + 1)

    return answer


if __name__ == '__main__':
    cases = [
        {'today': "2022.05.19", 'terms': ["A 6", "B 12", "C 3"],
         'privacies': ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]},
        {'today': "2020.01.01", 'terms': ["Z 3", "D 5"],
         'privacies': ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]}
    ]

    for case in cases:
        print(solution(case['today'], case['terms'], case['privacies']))