import math
import sys
import threading


def dfs(adj, used, v, n):
    if used[n - 1]:
        return
    used[v] = True
    for u, w in adj[v]:
        if not used[u - 1]:
            dfs(adj, used, u - 1, n)


def main():
    n, m = map(int, input().split())
    input_list = [list(map(int, input().split())) for _ in range(m)]

    adj = [[] for _ in range(n)]
    for el in input_list:
        v, u, w = el
        adj[v - 1].append((u, w))

    dp = [-math.inf for _ in range(n)]
    dp[0] = 0
    for d in range(1, n):
        for v in range(n):
            for (u, w) in adj[v]:
                if dp[v] != -math.inf:
                    dp[u - 1] = max(dp[u - 1], dp[v] + w)

    if dp[n - 1] == -math.inf:
        print(':(')
        exit(0)

    used = [False for _ in range(n)]
    changed = False
    for v in range(n):
        for (u, w) in adj[v]:
            if u - 1 == n - 1 and dp[u - 1] < dp[v] + w:
                changed = True
                break
            elif dp[u - 1] < dp[v] + w:
                dp[u - 1] = dp[v] + w
                dfs(adj, used, v, n)
                if used[n - 1]:
                    changed = True
                    break

    if not changed:
        print(dp[n - 1])
    else:
        print(':)')


if __name__ == '__main__':
    sys.setrecursionlimit(10000)
    threading.stack_size(100000)
    thread = threading.Thread(target=main)
    thread.start()