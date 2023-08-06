def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0

    have_to_deli = 0
    have_to_pick = 0

    for i in range(n):
        have_to_deli += deliveries[i]
        have_to_pick += pickups[i]

        while have_to_deli > 0 or have_to_pick > 0:
            have_to_deli -= cap
            have_to_pick -= cap
            answer += (n - i) * 2

    return answer


if __name__ == '__main__':
    cases = [
        {'cap': 4, 'n': 5, 'deliveries': [1, 0, 3, 1, 2], 'pickups': [0, 3, 0, 4, 0]},
        {'cap': 2, 'n': 7, 'deliveries': [1, 0, 2, 0, 1, 0, 2], 'pickups': [0, 2, 0, 1, 0, 2, 0]},
    ]

    for case in cases:
        print(solution(case['cap'], case['n'], case['deliveries'], case['pickups']))