from sys import stdin


class Solution:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        edges = []
        for line in stdin:
            edges.append(list(map(int, line.rstrip().split())))

        self.match = [-1 for _ in range(self.m)]
        self.adj = [[] for _ in range(self.n)]
        self.get_graph(edges)

        self.count = 0
        for v in range(self.n):
            used = [False for _ in range(self.n)]
            if self.dfs(v, used):
                self.count += 1

        covered_v_L = set()
        for idx, value in enumerate(self.match):
            if value != -1:
                covered_v_L.add(value)

        not_covered_v_L = set([i for i in range(self.n)]) - covered_v_L
        self.used_l = [False for _ in range(self.n)]
        self.used_r = [False for _ in range(self.m)]

        for v in not_covered_v_L:
            self.dfs_2(v)

        vc_l = []
        vc_r = []
        for i in range(self.n):
            if not self.used_l[i]:
                vc_l.append(i + 1)

        for i in range(self.m):
            if self.used_r[i]:
                vc_r.append(i + 1)

        len_l = len(vc_l)
        len_r = len(vc_r)
        print(len_l + len_r)
        print(len_l, len_r)
        print(*vc_l)
        print(*vc_r)

    def dfs_2(self, v):
        self.used_l[v] = True

        for u in self.adj[v]:
            if not self.used_r[u]:
                self.used_r[u] = True
                self.dfs_2(self.match[u])

    def dfs(self, v, used):
        if used[v]:
            return False
        used[v] = True

        for u in self.adj[v]:
            if self.match[u] == -1:
                self.match[u] = v
                return True
            if self.dfs(self.match[u], used):
                self.match[u] = v
                return True
        return False

    def get_graph(self, edges):
        for edge in edges:
            u, v = edge
            self.adj[u - 1].append(v - 1)


Solution()
