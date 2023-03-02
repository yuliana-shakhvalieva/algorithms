import sys
import threading
import itertools as it


def euler(v, adj, ans):
    while adj[v]:
        u = adj[v].pop()
        euler(u, adj, ans)
        ans.append([u, v])


def get_adj(d, k, nodes):
    adj = {}
    for node in nodes:
        adj[node] = []
        fix_prefix = node[:k - 2]
        for i in range(d):
            adj.get(node).append((i,) + fix_prefix)
    return adj


def main():
    d, k = map(int, input().split())
    list_d = []

    for i in range(d):
        list_d.append(i)

    if k == 1:
        print(*list_d, sep='')
    else:

        nodes = list(it.product(list_d, repeat=k - 1))
        adj = get_adj(d, k, nodes)

        ans = []
        euler(nodes[0], adj, ans)

        ans_final = [ans[0][0][i] for i in range(k - 1)]
        for i in range(len(ans)):
            ans_final.append(ans[i][1][k - 2])

        print(*ans_final, sep='')


if __name__ == "__main__":
    sys.setrecursionlimit(1000000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()
