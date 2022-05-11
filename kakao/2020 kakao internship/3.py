def solution(gems):
    answer = [0, 0]

    gem_unique = list(set(gems))
    result = []
    dp = [9999999] * len(gems)
    for i in range(len(gems)):
        now_have = []
        for k in range(i, len(gems)):
            now_have = gems[i:k+1]
            if sorted(list(set(now_have))) == sorted(gem_unique):
                print(now_have)
                if (dp[i] > len(now_have)):
                    result.append((i, k))
                    dp[i] = len(now_have)

    last_min = 99999
    for a, b in result:
        if b-a < last_min:
            last_min = b-a
            answer[0] = a+1
            answer[1] = b+1
    return answer


solution(["AA", "AB", "AC", "AA", "AC"])
