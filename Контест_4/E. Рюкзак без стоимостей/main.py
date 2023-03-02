def main():
    S, n = map(int, input().split())
    arr_weight = list(map(int, input().split()))

    dp = [0 for _ in range(S + 1)]
    dp[0] = 1

    for w in arr_weight:
        for i in range(S, w - 1, -1):
            if dp[i - w] == 1:
                dp[i] = 1

    for i in range(S, -1, -1):
        if dp[i] > 0:
            print(i)
            break


if __name__ == "__main__":
    main()
