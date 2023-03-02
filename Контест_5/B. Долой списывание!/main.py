import sys
import threading


def dfs(adj, color, v):
    for u in adj[v]:
        if color[u-1] == color[v]:
            return False
        elif color[u-1] == -1:
            color[u-1] = 1 - color[v]
            if not dfs(adj, color, u-1):
                return False
        elif color[u-1] != color[v]:
            pass
    return True


def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    adj = [[] for _ in range(n)]
    for edge in edges:
        adj[edge[0] - 1].append(edge[1])
        adj[edge[1] - 1].append(edge[0])

    color = [-1 for _ in range(n)]
    fail = False
    for v in range(n):
        if color[v] == -1:
            color[v] = 0
            if not dfs(adj, color, v):
                fail = True

    if not fail:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()
