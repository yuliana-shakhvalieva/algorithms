import sys
import threading
from sys import stdin


def dfs_2(cid, adj, v, num):
    cid[v] = num
    for u in adj[v]:
        if cid[u] == -1:
            dfs_2(cid, adj, u, num)


def dfs(used, adj, v, order):
    used[v] = True
    for u in adj[v]:
        if not used[u]:
            dfs(used, adj, u, order)
    order.append(v)


def make_graph(n, statements):
    adj = [[] for _ in range(2*n)]
    adj_rev = [[] for _ in range(2*n)]

    for statement in statements:
        if statement[1] == 0:
            if statement[3] == 0:
                adj[statement[0]].append(statement[2] + n)
                adj[statement[2]].append(statement[0] + n)

                adj_rev[statement[2] + n].append(statement[0])
                adj_rev[statement[0] + n].append(statement[2])
            else:
                adj[statement[0]].append(statement[2])
                adj[statement[2] + n].append(statement[0] + n)

                adj_rev[statement[2]].append(statement[0])
                adj_rev[statement[0] + n].append(statement[2] + n)
        else:
            if statement[3] == 0:
                adj[statement[0] + n].append(statement[2] + n)
                adj[statement[2]].append(statement[0])

                adj_rev[statement[2] + n].append(statement[0] + n)
                adj_rev[statement[0]].append(statement[2])
            else:
                adj[statement[0] + n].append(statement[2])
                adj[statement[2] + n].append(statement[0])

                adj_rev[statement[2]].append(statement[0] + n)
                adj_rev[statement[0]].append(statement[2] + n)

    return adj, adj_rev


def main():
    for line in stdin:
        n, m = [int(_) for _ in line.strip(' ').split()]
        statements = [[] for _ in range(m)]

        for i in range(m):
            a, b, c, d = map(int, input().split())
            statements[i].extend([a, b, c, d])

        adj, adj_rev = make_graph(n, statements)

        used = [False for _ in range(2*n)]
        order = []

        for v in range(2*n):
            if not used[v]:
                dfs(used, adj, v, order)

        order_rev = list(reversed(order))

        cid = [-1 for _ in range(2*n)]
        num = 0
        for v in order_rev:
            if cid[v] == -1:
                dfs_2(cid, adj_rev, v, num)
                num += 1

        ans = [-1 for _ in range(n)]
        for v in range(n):
            if cid[v] < cid[v + n]:
                ans[v] = 0
            elif cid[v] > cid[v + n]:
                ans[v] = 1

        print(*ans, sep='')


if __name__ == "__main__":
    sys.setrecursionlimit(100000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()
