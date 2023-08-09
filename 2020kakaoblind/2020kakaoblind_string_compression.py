def solution(s):
    answer = 0
    min_len = 1001
    for term_cnt in range(1, len(s)):
        term_lst = [s[i:i+term_cnt] for i in range(0, len(s), term_cnt)]

        res_str = ''
        cur_idx = 0
        comp_idx = 1
        same_cnt = 1
        while comp_idx < len(term_lst) and cur_idx < len(term_lst):
            if term_lst[cur_idx] == term_lst[comp_idx]:
                same_cnt += 1
                comp_idx += 1

                if comp_idx == len(term_lst):
                    res_str += f"{same_cnt}{term_lst[cur_idx]}"
            else:
                if same_cnt == 1:
                    res_str += f"{term_lst[cur_idx]}"
                else:
                    res_str += f"{same_cnt}{term_lst[cur_idx]}"

                cur_idx = comp_idx
                comp_idx += 1
                same_cnt = 1

                if comp_idx == len(term_lst):
                    if same_cnt == 1:
                        res_str += f"{term_lst[cur_idx]}"
                    else:
                        res_str += f"{same_cnt}{term_lst[cur_idx]}"

        if len(res_str) < min_len:
            min_len = len(res_str)
            answer = len(res_str)


    return answer


if __name__ == "__main__":
    cases = [
        {'s': "aabbaccc"},
        {'s': "ababcdcdababcdcd"},
        {'s': "abcabcdede"},
        {'s': "abcabcabcabcdededededede"},
        {'s': "xababcdcdababcdcd"},
    ]

    for case in cases:
        print(solution(case['s']))