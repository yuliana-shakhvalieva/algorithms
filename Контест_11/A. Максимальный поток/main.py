class Edge:
    def __init__(self, to, flow, cap, nxt):
        self.to = to
        self.flow = flow
        self.cap = cap
        self.nxt = nxt


class Graph:
    def __init__(self, n):
        self.edges = []
        self.head = [-1 for _ in range(n)]

    def add_edge(self, a, b, cap):
        self.edges.append(Edge(b, 0, cap, self.head[a]))
        self.head[a] = len(self.edges) - 1

        self.edges.append(Edge(a, 0, 0, self.head[b]))
        self.head[b] = len(self.edges) - 1


class Solution:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        self.graph = Graph(self.n)

        for _ in range(self.m):
            a, b, cap = map(int, input().split())
            self.graph.add_edge(a - 1, b - 1, cap)

        self.used = [False for _ in range(self.n)]

        ans = 0
        while delta := self.find_flow(0, int(1e9)):
            ans += delta
            self.used = [False for _ in range(self.n)]

        print(ans)

    def find_flow(self, v, max_cap):
        if self.used[v]:
            return 0

        if v == self.n - 1:
            return max_cap

        self.used[v] = True

        i = self.graph.head[v]
        while i != -1:
            limit = min(self.graph.edges[i].cap - self.graph.edges[i].flow, max_cap)

            if limit and (result := self.find_flow(self.graph.edges[i].to, limit)):
                self.graph.edges[i].flow += result
                self.graph.edges[i ^ 1].flow -= result
                return result

            i = self.graph.edges[i].nxt


Solution()
