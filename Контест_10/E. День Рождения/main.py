class Solution:
    def __init__(self):
        k = int(input())
        self.match = None
        self.adj = None

        for _ in range(k):
            self.m, self.n = map(int, input().split())
            edges = [list(map(int, input().split())) for _ in range(self.m)]
            self.solve(edges)

    def solve(self, edges):
        self.match = [-1 for _ in range(self.n)]
        self.adj = [-1 for _ in range(self.m)]
        self.get_inverted_graph(edges)
        vc_l, vc_r = self.find_vc()
        independent_set_l = set([i for i in range(1, self.m+1)]) - vc_l
        independent_set_r = set([i for i in range(1, self.n+1)]) - vc_r

        len_l, len_r = len(independent_set_l), len(independent_set_r)

        print(len_l + len_r)
        print(len_l, len_r)
        print(*independent_set_l)
        print(*independent_set_r)

    def find_vc(self):
        for v in range(self.m):
            used = [False for _ in range(self.m)]
            self.dfs(v, used)

        covered_v_L = set()
        for idx, value in enumerate(self.match):
            if value != -1:
                covered_v_L.add(value)

        not_covered_v_L = set([i for i in range(self.m)]) - covered_v_L
        used_l = [False for _ in range(self.m)]
        used_r = [False for _ in range(self.n)]

        for v in not_covered_v_L:
            self.dfs_2(v, used_l, used_r)

        vc_l = []
        vc_r = []
        for i in range(self.m):
            if not used_l[i]:
                vc_l.append(i+1)

        for i in range(self.n):
            if used_r[i]:
                vc_r.append(i+1)

        return set(vc_l), set(vc_r)

    def dfs_2(self, v, used_l, used_r):
        used_l[v] = True

        for u in self.adj[v]:
            if not used_r[u]:
                used_r[u] = True
                self.dfs_2(self.match[u], used_l, used_r)

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

    def get_inverted_graph(self, edges):
        for idx, edge in enumerate(edges):
            self.adj[idx] = [i for i in range(self.n)]
            if edge[0] == 0:
                continue
            else:
                for e in edge[:-1]:
                    self.adj[idx].remove(e - 1)


Solution()
