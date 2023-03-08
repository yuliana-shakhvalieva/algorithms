import math


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
        self.dist = None
        self.n, self.m = map(int, input().split())
        self.graph = Graph(self.n)

        for _ in range(self.m):
            a, b, cap = map(int, input().split())
            self.graph.add_edge(a - 1, b - 1, cap)

        ans = 0
        while self.bfs():
            headcopy = list(self.graph.head)

            while delta := self.find_flow(0, int(1e9), headcopy):
                ans += delta

        print(ans)

        for i in range(0, len(self.graph.edges), 2):
            edge = self.graph.edges[i]
            print(edge.flow)

    def bfs(self):
        q = [0]
        self.dist = [math.inf for _ in range(self.n)]
        self.dist[0] = 0
        while q:
            v = q.pop(0)
            e = self.graph.head[v]

            while e != -1:
                u = self.graph.edges[e].to
                if self.graph.edges[e].flow < self.graph.edges[e].cap and self.dist[u] == math.inf:
                    self.dist[u] = self.dist[v] + 1
                    q.append(u)
                e = self.graph.edges[e].nxt

        return self.dist[self.n - 1] != math.inf

    def find_flow(self, v, max_cap, head):
        if v == self.n - 1:
            return max_cap

        while True:
            e = head[v]
            if e == -1:
                return 0

            u = self.graph.edges[e]
            limit = min(u.cap - u.flow, max_cap)

            if limit and self.dist[u.to] == self.dist[v] + 1 and (result := self.find_flow(u.to, limit, head)):
                self.graph.edges[e].flow += result
                self.graph.edges[e ^ 1].flow -= result
                return result
            else:
                head[v] = u.nxt


Solution()
