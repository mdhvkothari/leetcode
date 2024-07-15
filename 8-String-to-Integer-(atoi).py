def myAtoi(s: str) -> int:
    #  defining int max and min range
    INT_MAX, INT_MIN = (2**31) - 1, -1*(2**31)

    num , sign, l, index = 0, 1, len(s), 0
    
    # first count spaces if there is any
    while index < l and s[index] == ' ':
        index += 1

    # store the sign in a sign variable so that we can use later
    if index < l and (s[index] == "+" or s[index] == "-"):
        if s[index] == "-":
            sign = -1
        index += 1
    
    # calculating the number
    while index < l and ord(s[index]) >= ord("0") and ord(s[index]) <= ord("9"):
        num = num*10 + int(s[index])
        index += 1
    
    num *= sign  # multiple by sign after calculation the number
    return min(max(num, INT_MIN), INT_MAX)



