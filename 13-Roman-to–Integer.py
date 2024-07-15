def romanToInt(s: str) -> int:
    # defining dic to map against ever roman number
    m = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    ans = 0
    for i in range(len(s)):
        if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:  # suppose we have CM C(100) < M(1000) then we will subtract 1000 - 100 which is CM - 900
            ans -= m[s[i]]
        else:
            ans += m[s[i]]
    return ans