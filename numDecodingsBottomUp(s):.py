def numDecodingsBottomUp(s):
    memo = [0] * (len(s) + 1)
    memo[0] = 1

    for i, x in enumerate(s):
        if x != '0' and memo[i]:
            memo[i+1] += memo[i]
            if i+1 < len(s) and s[i:i+2] <= '26':
                memo[i+2] += memo[i]
    return memo[-1]

