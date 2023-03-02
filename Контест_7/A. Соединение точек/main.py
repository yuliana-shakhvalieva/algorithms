def get(x, p):
    if p[x] != x:
        ans = get(p[x], p)
        p[x] = ans
        return ans
    else:
        return x


def merge(x, y, p, rank):
    x = get(x, p)
    y = get(y, p)
    if rank[x] > rank[y]:
        x, y = y, x
    elif rank[x] == rank[y]:
        rank[y] += 1
    p[x] = y


def count_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** (1/2)


def make_sort_graph(points):
    edges = []
    n = len(points)
    for i in range(n):
        for j in range(i+1, n):
            edges.append((i+1, j+1, count_distance(points[i], points[j])))

    edges = sorted(edges, key=lambda x: x[2])

    return edges


def main():
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]
    edges = make_sort_graph(points)
    p = [i for i in range(n)]
    rank = [1 for _ in range(n)]
    mst = []
    length = 0

    for edge in edges:
        u, v = edge[0]-1, edge[1]-1
        get_u, get_v = get(u, p), get(v, p)
        if get_u != get_v:
            merge(get_u, get_v, p, rank)
            mst.append((edge[0], edge[1]))
            length += edge[2]

    print('{0:.6f}'.format(length))
    print(len(mst))
    for el in mst:
        print(*el)


if __name__ == "__main__":
    main()
