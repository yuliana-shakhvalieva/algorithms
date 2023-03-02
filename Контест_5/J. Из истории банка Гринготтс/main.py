import sys
import threading


def add_edges(adj, odds):
    adj_2 = adj.copy()
    edges = set()
    adj_2.append(set())

    for v in odds:
        adj_2[-1].add(v)
        adj_2[v].add(len(adj))
        edges.add((v, len(adj)))
        edges.add((len(adj), v))

    return edges, adj_2


def euler(v, adj_2, path):
    while adj_2[v]:
        u = adj_2[v].pop()
        adj_2[u].remove(v)
        euler(u, adj_2, path)
        path.append(u)


def main():
    n, m = map(int, input().split())
    adj = [set() for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().split())
        adj[a - 1].add(b - 1)
        adj[b - 1].add(a - 1)

    odds = set()
    for v in range(n):
        if len(adj[v]) % 2 != 0:
            odds.add(v)

    path = []

    if not odds:
        euler(0, adj, path)
    else:
        edges, adj_2 = add_edges(adj, odds)
        euler(len(adj), adj_2, path)

    ans = [[]]
    if path[0] == len(adj):
        path = path[1:]

    for el in path:
        if el == len(adj):
            ans.append([])
        else:
            ans[-1].append(str(el+1))

    if not odds:
        ans[0].append(ans[0][0])

    print(len(ans))

    for el in ans:
        print(*el)


if __name__ == '__main__':
    sys.setrecursionlimit(400000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()
