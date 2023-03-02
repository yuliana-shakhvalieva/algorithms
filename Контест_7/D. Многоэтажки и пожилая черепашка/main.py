import sys
import threading


def dfs(v, adj, used, build, reachable):
    used[v] = True

    for u in adj[v]:
        reachable[u] = True
        if not used[u] and not build[u]:
            dfs(u, adj, used, build, reachable)


def get_adj(n, m):
    adj = [[] for _ in range(n * m)]

    for i in range(n * m - 1):
        if (i + 1) % m == 0:
            adj[i].append(i + m)
        elif i + 1 > m * (n - 1):
            adj[i].append(i + 1)
        else:
            adj[i].append(i + 1)
            adj[i].append(i + m)

    return adj


def main():
    n, m, k = map(int, input().split())

    requests = []
    build = [False for _ in range(n * m)]
    used = [False for _ in range(n * m)]
    reachable = [False for _ in range(n * m)]
    reachable[0] = True

    for i in range(k):
        x, y = map(int, input().split())
        request = (x - 1) * m + y - 1
        requests.append(request)
        build[request] = True

    adj = get_adj(n, m)
    dfs(0, adj, used, build, reachable)

    if used[-1]:
        print(-1)
    else:
        for i in range(k-1, -1, -1):
            request = requests[i]
            build[request] = False
            if reachable[request]:
                dfs(request, adj, used, build, reachable)
            if used[-1] and not build[-1]:
                print(i+1)
                break


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()
