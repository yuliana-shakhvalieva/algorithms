def main():
    str_1 = list(input())
    str_2 = list(input())

    n = len(str_1)
    m = len(str_2)
    dp = [[0 for _ in range(m)] for _ in range(n)]

    if str_1[0] == str_2[0]:
        dp[0][0] = 0
    else:
        dp[0][0] = 1

    for i in range(1, n):
        if str_1[i] == str_2[0]:
            dp[i][0] = i
        else:
            dp[i][0] = dp[i - 1][0] + 1

    for j in range(1, m):
        if str_1[0] == str_2[j]:
            dp[0][j] = j
        else:
            dp[0][j] = dp[0][j - 1] + 1

    for i in range(1, n):
        for j in range(1, m):
            if str_1[i] == str_2[j]:
                dp[i][j] = min(dp[i - 1][j] + 1,
                               dp[i][j - 1] + 1,
                               dp[i - 1][j - 1])
            else:
                dp[i][j] = min(dp[i - 1][j] + 1,
                               dp[i][j - 1] + 1,
                               dp[i - 1][j - 1] + 1)

    print(dp[len(str_1) - 1][len(str_2) - 1])


if __name__ == "__main__":
    main()
