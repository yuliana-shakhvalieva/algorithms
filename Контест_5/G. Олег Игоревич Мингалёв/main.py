import sys
import threading


def distance_square(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2


def get_cnf(m, coordinates, n):
    cnf = []
    for i in range(n):
        for j in range(i + 1, n):
            if distance_square(coordinates[i][0],
                               coordinates[i][1],
                               coordinates[j][0],
                               coordinates[j][1]) < m:
                cnf.append([2 * i + 1, 2 * j + 1])

            if distance_square(coordinates[i][0],
                               coordinates[i][1],
                               coordinates[j][2],
                               coordinates[j][3]) < m:
                cnf.append([2 * i + 1, 2 * j])

            if distance_square(coordinates[i][2],
                               coordinates[i][3],
                               coordinates[j][0],
                               coordinates[j][1]) < m:
                cnf.append([2 * i, 2 * j + 1])

            if distance_square(coordinates[i][2],
                               coordinates[i][3],
                               coordinates[j][2],
                               coordinates[j][3]) < m:

                cnf.append([2 * i, 2 * j])
    return cnf


def make_graph(cnf, n):
    adj = [[] for _ in range(2 * n)]
    adj_rev = [[] for _ in range(2 * n)]

    for i in range(len(cnf)):
        a, b = cnf[i][0], cnf[i][1]
        neg_a, neg_b = a ^ 1, b ^ 1

        adj[neg_a].append(b)
        adj[neg_b].append(a)

        adj_rev[b].append(neg_a)
        adj_rev[a].append(neg_b)

    return adj, adj_rev


def dfs(v, order, used, adj):
    used[v] = True
    for u in adj[v]:
        if not used[u]:
            dfs(u, order, used, adj)
    order.append(v)


def dfs2(v, c, used, colors, adj_rev):
    used[v] = True
    colors[v] = c
    for u in adj_rev[v]:
        if not used[u]:
            if colors[u] == 0:
                dfs2(u, c, used, colors, adj_rev)


def find_scc(adj, adj_rev, n):
    used = [False for _ in range(2 * n)]
    order = []

    for v in range(2 * n):
        if not used[v]:
            dfs(v, order, used, adj)

    colors = [0 for _ in range(2 * n)]
    used = [False for _ in range(2 * n)]
    c = 1
    order.reverse()

    for v in order:
        if not used[v]:
            dfs2(v, c, used, colors, adj_rev)
            c += 1
    return colors


def find_solution(scc, n):
    for i in range(0, 2 * n, 2):
        if scc[i] == scc[i + 1]:
            return False
    return True


def check_answer(m, coordinates, n):
    cnf = get_cnf(m, coordinates, n)
    adj, adj_rev = make_graph(cnf, n)
    scc = find_scc(adj, adj_rev, n)
    if find_solution(scc, n):
        return True
    else:
        return False


def main():
    n = int(input())
    coordinates = [list(map(int, input().split())) for _ in range(n)]

    left = 0
    right = 8 * 10 ** 18
    mid = left + (right - left) // 2

    while right - left > 1:
        if check_answer(mid, coordinates, n):
            left = mid
        else:
            right = mid
        mid = left + (right - left) // 2

    print(left ** 0.5)


if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()
