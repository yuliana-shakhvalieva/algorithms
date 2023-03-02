import sys
import threading


def dfs_2(cid, adj, v, num, delegates):
    cid[v] = num
    delegates[num] = v + 1
    for u in adj[v]:
        if cid[u - 1] == -1:
            dfs_2(cid, adj, u - 1, num, delegates)


def dfs(used, adj, v, order):
    used[v] = True
    for u in adj[v]:
        if not used[u - 1]:
            dfs(used, adj, u - 1, order)
    order.append(v + 1)


def main():
    n = int(input())
    m = int(input())
    edges = [list(map(int, input().split())) for _ in range(m)]

    adj = [[] for _ in range(n)]
    adj_rev = [[] for _ in range(n)]
    for i in range(m):
        adj[edges[i][0] - 1].append(edges[i][1])
        adj_rev[edges[i][1] - 1].append(edges[i][0])

    used = [False for _ in range(n)]
    order = []

    for v in range(n):
        if not used[v]:
            dfs(used, adj, v, order)

    order_rev = list(reversed(order))

    cid = [-1 for _ in range(n)]
    delegates = [-1 for _ in range(n)]
    num = 0
    for v in order_rev:
        if cid[v - 1] == -1:
            dfs_2(cid, adj_rev, v - 1, num, delegates)
            num += 1

    stocks = [True for _ in range(len(cid))]
    for edge in edges:
        if cid[edge[0] - 1] != cid[edge[1] - 1]:
            stocks[cid[edge[0] - 1]] = False

    ans = []
    for stock, delegate in zip(stocks, delegates):
        if stock and delegate != -1:
            ans.append(delegate)

    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    threading.stack_size(100000)
    thread = threading.Thread(target=main)
    thread.start()
