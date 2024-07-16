def beautySum(s: str) -> int:
    result = 0
    for i in range(len(s)):
        dic = {}
        for j in range(i, len(s)):
            if s[j] not in dic.keys():
                dic[s[j]] = 1
            else:
                dic[s[j]] += 1
            min_count, max_count = min(dic.values()), max(dic.values())
            result += (max_count - min_count)
    return result
        