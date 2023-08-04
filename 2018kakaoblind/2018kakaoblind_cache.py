def solution(cacheSize, cities):
    answer = 0

    cache = []
    for ref in cities:
        if not ref in cache:
            if len(cache) < cacheSize:
                cache.append(ref)
            elif len(cache) == 0:
                cache.append(ref)
            else:
                cache.pop(0)
                cache.append(ref)

            answer += 5
        else:
            cache.pop(cache.index(ref))
            cache.append(ref)

            answer += 1

    return answer


if __name__ == '__main__':
    cases = [
        {'cacheSize': 3, 'cities': ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]},
        {'cacheSize': 3, 'cities': ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]},
        {'cacheSize': 2, 'cities': ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]},
        {'cacheSize': 5, 'cities': ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]},
        {'cacheSize': 2, 'cities': ["Jeju", "Pangyo", "NewYork", "NewYork"]},
        {'cacheSize': 0, 'cities': ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]},
    ]

    for case in cases:
        print(solution(case['cacheSize'], case['cities']))