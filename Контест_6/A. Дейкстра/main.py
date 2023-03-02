import heapq
import math


def main():
    N, S, F = map(int, input().split())
    S -= 1
    F -= 1

    adj = [[(idx, el) for idx, el in enumerate(list(map(int, input().split()))) if el > 0] for _ in range(N)]

    H = []
    d = [math.inf for _ in range(N)]
    d[S] = 0
    heapq.heappush(H, (d[S], S))
    while H:
        dv, v = heapq.heappop(H)
        if dv <= d[v]:
            for u, w in adj[v]:
                if d[v] + w < d[u]:
                    d[u] = d[v] + w
                    heapq.heappush(H, (d[u], u))

    if d[F] == math.inf:
        print(-1)
    else:
        print(d[F])


if __name__ == "__main__":
    main()
