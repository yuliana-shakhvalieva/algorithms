import sys
import threading


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


def make_graph(n, lines, connectors, dictionary):
    n_2 = 2 * n
    n_4 = 4 * n
    adj = [[] for _ in range(n_4)]
    adj_rev = [[] for _ in range(n_4)]

    if lines[connectors[0] - 1] == lines[connectors[n_2 - 1] - 1]:
        adj[0].append(n_2 - 1 + n_2)
        adj[n_2 - 1].append(n_2)

        adj_rev[n_2 - 1 + n_2].append(0)
        adj_rev[n_2].append(n_2 - 1)

    for i in range(1, n_2):
        if lines[connectors[i] - 1] == lines[connectors[i-1] - 1]:
            adj[i].append(i - 1 + n_2)
            adj[i-1].append(i + n_2)

            adj_rev[i - 1 + n_2].append(i)
            adj_rev[i + n_2].append(i-1)

    for key, value in dictionary.items():
        adj[value[0] + n_2].append(value[1])
        adj[value[1] + n_2].append(value[0])
        adj[value[0]].append(value[1] + n_2)
        adj[value[1]].append(value[0] + n_2)

        adj_rev[value[1]].append(value[0] + n_2)
        adj_rev[value[0]].append(value[1] + n_2)
        adj_rev[value[1] + n_2].append(value[0])
        adj_rev[value[0] + n_2].append(value[1])

    return adj, adj_rev


def main():
    n = int(input())
    lines = list(map(int, input().split()))
    connectors = list(map(int, input().split()))

    dictionary = {}
    for i in range(n):
        dictionary[i + 1] = []

    for idx, connector in enumerate(connectors):
        dictionary.get(connector).append(idx)

    adj, adj_rev = make_graph(n, lines, connectors, dictionary)
    n_4 = 4 * n
    n_2 = 2 * n

    used = [False for _ in range(n_4)]
    order = []

    for v in range(n_4):
        if not used[v]:
            dfs(used, adj, v, order)

    order_rev = list(reversed(order))

    cid = [-1 for _ in range(n_4)]
    num = 0
    for v in order_rev:
        if cid[v] == -1:
            dfs_2(cid, adj_rev, v, num)
            num += 1

    flag = True
    pre_ans = [-1 for _ in range(n_2)]
    for v in range(n_2):
        if cid[v] < cid[v + n_2]:
            pre_ans[v] = 0
        elif cid[v] > cid[v + n_2]:
            pre_ans[v] = 1
        elif cid[v] == cid[v + n_2]:
            flag = False
            break

    ans = [-1 for _ in range(n)]
    for idx, el in enumerate(pre_ans):
        if el == 1:
            ans[connectors[idx] - 1] = idx + 1

    if flag:
        print('YES')
        print(*ans)
    else:
        print('NO')


if __name__ == "__main__":
    sys.setrecursionlimit(210000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()
