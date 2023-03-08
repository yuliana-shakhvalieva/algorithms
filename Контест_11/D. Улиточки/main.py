import math
import sys
import threading
from collections import deque


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
        self.n, self.m, self.s, self.t = map(int, input().split())
        self.graph = self.built_graph()
        max_flow = self.dinic_algo()

        if max_flow >= 2:
            print('YES')
            for _ in range(2):
                self.path = []
                self.dfs(self.s - 1)
                print(*self.path)
        else:
            print('NO')

    def dfs(self, v):
        self.path.append(v + 1)
        if v == self.t - 1:
            return
        e = self.graph.head[v]

        while self.graph.edges[e].flow > 0:
            u = self.graph.edges[e].to
            self.graph.head[v] = self.graph.edges[e].nxt
            self.dfs(u)
            break
        else:
            while self.graph.edges[e].flow <= 0:
                e = self.graph.edges[e].nxt
            u = self.graph.edges[e].to
            self.graph.head[v] = self.graph.edges[e].nxt
            self.dfs(u)

    def dinic_algo(self):
        max_flow = 0
        while self.bfs():
            headcopy = list(self.graph.head)
            while delta := self.find_flow(self.s - 1, int(1e9), headcopy):
                max_flow += delta
        return max_flow

    def bfs(self):
        q = deque()
        q.append(self.s - 1)
        self.dist = [math.inf for _ in range(self.n)]
        self.dist[self.s - 1] = 0
        while q:
            v = q.popleft()
            e = self.graph.head[v]
            while e != -1:
                u = self.graph.edges[e].to
                if self.graph.edges[e].flow < self.graph.edges[e].cap and self.dist[u] == math.inf:
                    self.dist[u] = self.dist[v] + 1
                    q.append(u)
                e = self.graph.edges[e].nxt

        return self.dist[self.t - 1] != math.inf

    def find_flow(self, v, max_cap, head):
        if v == self.t - 1:
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

    def built_graph(self):
        graph = Graph(self.n)

        for _ in range(self.m):
            a, b = map(int, input().split())
            graph.add_edge(a - 1, b - 1, 1)

        return graph


def main():
    Solution()


if __name__ == '__main__':
    sys.setrecursionlimit(200000)
    threading.stack_size(100000000)
    thread = threading.Thread(target=main)
    thread.start()

