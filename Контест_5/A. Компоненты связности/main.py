import sys
import threading


def dfs(adj, used, a_color, v, color):

    a_color[v] = color
    used[v] = True
    for u in adj[v]:
        if not used[u-1]:
            dfs(adj, used, a_color, u-1, color)


def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    adj = [[] for _ in range(n)]
    for edge in edges:
        adj[edge[0] - 1].append(edge[1])
        adj[edge[1] - 1].append(edge[0])

    color, count = 1, 0

    used = [False for _ in range(n)]
    a_color = [-1 for _ in range(n)]
    for v in range(n):
        if not used[v]:
            dfs(adj, used, a_color, v, color)
            count += 1
            color += 1

    print(count)
    print(' '.join(str(el) for el in a_color))


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()
