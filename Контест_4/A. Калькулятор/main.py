def main():
    N = int(input())
    dp = [0 for _ in range(N)]
    parent = [0 for _ in range(N)]

    for i in range(1, N):

        idx_1 = i - 1
        idx_2 = (i + 1) // 2 - 1
        idx_3 = (i + 1) // 3 - 1

        if (i + 1) % 2 == 0 and (i + 1) % 3 == 0:
            min_dp = min((dp[idx_1], idx_1), (dp[idx_2], idx_2), (dp[idx_3], idx_3))
            dp[i] = min_dp[0] + 1
            parent[i] = min_dp[1]
        elif (i + 1) % 2 == 0 and (i + 1) % 3 != 0:
            min_dp = min((dp[idx_1], idx_1), (dp[idx_2], idx_2))
            dp[i] = min_dp[0] + 1
            parent[i] = min_dp[1]
        elif (i + 1) % 2 != 0 and (i + 1) % 3 == 0:
            min_dp = min((dp[idx_1], idx_1), (dp[idx_3], idx_3))
            dp[i] = min_dp[0] + 1
            parent[i] = min_dp[1]
        elif (i + 1) % 2 != 0 and (i + 1) % 3 != 0:
            dp[i] = dp[i - 1] + 1
            parent[i] = i - 1

    ans = [N]
    j = N - 1
    while j != 0:
        ans.append(parent[j] + 1)
        j = parent[j]

    print(dp[N - 1])
    print(' '.join([str(ans[i]) for i in range(len(ans) - 1, -1, -1)]))


if __name__ == "__main__":
    main()
