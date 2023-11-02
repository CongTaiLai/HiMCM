# Subsequence: derived fromt another sequence by deleting any number of elements without changing the order of the remainings.
def longest_common_subsequence(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):  # m*i
        for j in range(1, n + 1):  # n*j
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct the LCS
    lcs = []
    parameters = []
    i, j = m, n
    while i > 0 and j > 0:
        parameters.append((i, j))
        if s1[i - 1] == s2[j - 1]:  # if colored, left+up
            lcs.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:  # if up>left, up
            i -= 1
        else:  # left>=up, left
            j -= 1



    return ''.join(reversed(lcs))


s1 = "AGGTAB"
s2 = "GXTXAYB"
result = longest_common_subsequence(s1, s2)
print("Longest Common Subsequence:", result)
