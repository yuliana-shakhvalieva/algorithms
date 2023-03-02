import sys
import threading


def dfs_2(cid, adj, v, num):
    cid[v] = num
    for u in adj[v]:
        if cid[u-1] == -1:
            dfs_2(cid, adj, u-1, num)


def dfs(used, adj, v, order):
    used[v] = True
    for u in adj[v]:
        if not used[u-1]:
            dfs(used, adj, u-1, order)
    order.append(v+1)


def get_adj(edges, adj):
    for edge in edges:
        adj[edge[0] - 1].append(edge[1])
    return adj


def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    adj = get_adj(edges, [[] for _ in range(n)])

    used = [False for _ in range(n)]
    order = []

    for v in range(n):
        if not used[v]:
            dfs(used, adj, v, order)

    order_rev = list(reversed(order))

    edges_rev = []
    for edge in edges:
        left, right = edge[0], edge[1]
        edges_rev.append([right, left])

    adj_rev = get_adj(edges_rev, [[] for _ in range(n)])
    cid = [-1 for _ in range(n)]
    num = 0
    for v in order_rev:
        if cid[v-1] == -1:
            dfs_2(cid, adj_rev, v-1, num)
            num += 1

    cond = set()
    for edge in edges:
        if cid[edge[0] - 1] != cid[edge[1] - 1]:
            cond.add((cid[edge[0] - 1], cid[edge[1] - 1]))

    print(len(cond))


if __name__ == "__main__":
    sys.setrecursionlimit(200000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()
