import heapq
import math


def main():
    N = int(input())

    adj = [[(idx, el) for idx, el in enumerate(list(map(int, input().split()))) if el > 0] for _ in range(N)]

    eccentricity = [-1 for _ in range(N)]
    for i in range(N):
        H = []
        d = [math.inf for _ in range(N)]
        d[i] = 0
        heapq.heappush(H, (d[i], i))
        while H:
            dv, v = heapq.heappop(H)
            if dv <= d[v]:
                for u, w in adj[v]:
                    if d[v] + w < d[u]:
                        d[u] = d[v] + w
                        heapq.heappush(H, (d[u], u))
        max_d = -1
        for el in d:
            if el != math.inf and el > max_d:
                max_d = el

        eccentricity[i] = max_d

    diameter = -1
    radius = math.inf
    for el in eccentricity:
        if el != -1 and el > diameter:
            diameter = el
        if el != -1 and el < radius:
            radius = el
    print(diameter)
    print(radius)


if __name__ == "__main__":
    main()
