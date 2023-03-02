def count_dp(n, m, m_arr, c_arr):
    dp = [[100 for _ in range(m + 1)] for _ in range(n + 1)]

    for j in range(m + 1):
        dp[0][j] = 0

    for i in range(n + 1):
        dp[i][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if j >= m_arr[i - 1]:
                dp[i][j] = max(dp[i - 1][j - m_arr[i - 1]] + c_arr[i - 1], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    return dp


def recover_answer(dp, ans, m_arr, i, j):
    if dp[i][j] == 0:
        return
    if dp[i - 1][j] == dp[i][j]:
        recover_answer(dp, ans, m_arr, i - 1, j)
    else:
        recover_answer(dp, ans, m_arr, i - 1, j - m_arr[i - 1])
        ans.append(i)
    return ans


def main():
    n, m = map(int, input().split())
    m_arr = list(map(int, input().split()))
    c_arr = list(map(int, input().split()))

    dp = count_dp(n, m, m_arr, c_arr)
    ans = recover_answer(dp, [], m_arr, n, m)

    if ans is None:
        print(0)
        print()
    else:
        print(len(ans))
        print(' '.join(str(el) for el in ans))


if __name__ == "__main__":
    main()
