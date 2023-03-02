def get(x, p):
    while p[x] != x:
        x = p[x]
    return x


def merge(x, y, p, rank, points):
    x = get(x, p)
    y = get(y, p)
    if x == y:
        return
    elif rank[x] > rank[y]:
        x, y = y, x
    elif rank[x] == rank[y]:
        rank[y] += 1
    p[x] = y
    points[x] -= points[y]


def add(x, v, points, p):
    x = get(x, p)
    points[x] += v


def get_points(x, points, p):
    exp = 0
    while p[x] != x:
        exp += points[x]
        x = p[x]
    exp += points[x]
    return exp


def main():
    n, m = map(int, input().split())
    requests = [list(map(str, input().split())) for _ in range(m)]

    p = [i for i in range(n)]
    rank = [1 for _ in range(n)]
    points = [0 for _ in range(n)]

    for request in requests:
        if request[0] == 'add':
            add(int(request[1]) - 1, int(request[2]), points, p)
        elif request[0] == 'join':
            merge(int(request[1]) - 1, int(request[2]) - 1, p, rank, points)
        elif request[0] == 'get':
            print(get_points(int(request[1]) - 1, points, p))


if __name__ == '__main__':
    main()
