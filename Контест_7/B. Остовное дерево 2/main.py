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


def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]
    edges = sorted(edges, key=lambda x: x[2])

    p = [i for i in range(n)]
    rank = [1 for _ in range(n)]
    length = 0

    for edge in edges:
        u, v = edge[0] - 1, edge[1] - 1
        get_u, get_v = get(u, p), get(v, p)
        if get_u != get_v:
            merge(get_u, get_v, p, rank)
            length += edge[2]

    print(length)


if __name__ == "__main__":
    main()
