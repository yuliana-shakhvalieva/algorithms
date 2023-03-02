import sys
import threading

ans = []
end = None

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

used = [0 for _ in range(n + 1)]


def find_cycle(adj, v):
    global end
    used[v] = 1
    ans.append(v)
    for u in adj[v]:
        if not used[u] and find_cycle(adj, u):
            return True
        elif used[u] == 1:
            end = u
            return True
        elif used[u] == 2:
            pass
    ans.pop()
    used[v] = 2
    return False


def main():
    adj = [[] for _ in range(n + 1)]
    for edge in edges:
        adj[edge[0]].append(edge[1])

    for v in range(1, n + 1):
        if not used[v]:
            cycle = find_cycle(adj, v)
        if cycle:
            break

    if not cycle:
        print("NO")
    else:
        print("YES")
        for i in range(len(ans) - 1, -1, -1):
            if ans[i] == end:
                break
        print(*ans[i:])


if __name__ == "__main__":
    sys.setrecursionlimit(200000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()
