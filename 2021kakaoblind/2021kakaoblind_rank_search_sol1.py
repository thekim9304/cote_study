'''
https://school.programmers.co.kr/learn/courses/30/lessons/72412
- 단순 필터링
'''


def solution1(info, query):
    '''
    단순 필터링
    정확성 통과
    효율성 탈락
    '''
    answer = []

    info_dict_lst = []
    for info_str in info:
        lang, tech, career, food, score = info_str.split()
        info_dict_lst.append({'lang': lang, 'tech': tech, 'career': career, 'food': food, 'score': int(score)})

    for q in query:
        q = q.replace(" and ", " ")
        lang, tech, career, food, score = q.split()
        score = int(score)

        if lang != '-':
            target = list(filter(lambda x: x['lang'] == lang, info_dict_lst))
        else:
            target = info_dict_lst
        if tech != '-':
            target = list(filter(lambda x: x['tech'] == tech, target))
        if career != '-':
            target = list(filter(lambda x: x['career'] == career, target))
        if food != '-':
            target = list(filter(lambda x: x['food'] == food, target))
        target = list(filter(lambda x: x['score'] >= score, target))

        answer.append(len(target))

    return answer


if __name__ == '__main__':
    cases = [
        {'info': ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
         'query': ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]}
    ]

    for case in cases:
        print(solution1(case['info'], case['query']))