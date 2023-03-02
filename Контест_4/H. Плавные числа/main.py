def main():
    n = int(input())

    dp = [1] * 10
    dp[0] = 0

    for k in range(n - 1):
        hlp = [0] * 10
        hlp[0] = dp[0] + dp[1]
        hlp[9] = dp[8] + dp[9]

        for i in range(1, 9):
            hlp[i] = dp[i - 1] + dp[i] + dp[i + 1]

        dp = hlp.copy()

    print(sum(dp))


if __name__ == "__main__":
    main()



