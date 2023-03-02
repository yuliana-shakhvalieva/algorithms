def main():
    n = int(input())

    dp = [[0 for _ in range(10)] for _ in range(n)]

    steps = {1: (8, 6),
             2: (7, 9),
             3: (4, 8),
             4: (9, 3, 0),
             5: (),
             6: (7, 1, 0),
             7: (6, 2),
             8: (3, 1),
             9: (2, 4),
             0: (6, 4)}

    for i in range(10):
        if i != 0 and i != 8:
            dp[0][i] = 1

    for k in range(1, n):
        for key, value in steps.items():
            for i in value:
                dp[k][key] += dp[k-1][i]

    ans = sum(dp[n-1])
    print(ans % 1000000000)


if __name__ == "__main__":
    main()



