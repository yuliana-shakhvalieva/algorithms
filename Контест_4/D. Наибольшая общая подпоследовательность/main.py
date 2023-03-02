def main():
    n = int(input())
    seq_n = list(map(int, input().split()))
    m = int(input())
    seq_m = list(map(int, input().split()))
    dp = [[-1 for _ in range(m)] for _ in range(n)]

    for j in range(m):
        if seq_n[0] == seq_m[j]:
            dp[0][j] = 1
        else:
            dp[0][j] = 0

    for i in range(n):
        if seq_n[i] == seq_m[0]:
            dp[i][0] = 1
        else:
            dp[i][0] = 0

    for i in range(1, n):
        for j in range(1, m):
            if seq_n[i] == seq_m[j]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    print(dp[n - 1][m - 1])


if __name__ == "__main__":
    main()
