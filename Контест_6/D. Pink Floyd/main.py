import math


def main():
    n, m, k = map(int, input().split())
    flights = [list(map(int, input().split())) for _ in range(m)]
    concerts = list(map(int, input().split()))

    par = [[0 for _ in range(n)] for _ in range(n)]
    adj = [[] for _ in range(n)]
    ends = []

    for idx, el in enumerate(flights):
        v, u, w = el
        adj[v - 1].append((u, w, idx + 1))
        par[v - 1][u - 1] = idx
        ends.append(u - 1)

    dp = [[-math.inf for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dp[i][j] = 0
            for el in adj[i]:
                if el[0] - 1 == j:
                    dp[i][j] = el[1]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = min(dp[i][j], math.inf)
                if dp[i][j] < dp[i][k] + dp[k][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]
                    par[i][j] = par[i][k]

    for c in concerts:
        if dp[c - 1][c - 1] > 0:
            print('infinitely kind')
            exit(0)

    ans = []
    for c in range(1, len(concerts)):
        s = concerts[c - 1] - 1
        f = concerts[c] - 1
        cur = par[s][f]
        help_arr = [cur + 1]
        while ends[cur] != f:
            if dp[ends[cur]][ends[cur]] > 0:
                print('infinitely kind')
                exit(0)
            cur = par[ends[cur]][f]
            help_arr.append(cur + 1)
        for el in help_arr:
            ans.append(el)

    print(len(ans))
    print(*ans)


if __name__ == '__main__':
    main()
