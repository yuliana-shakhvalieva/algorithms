class Solution:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        edges = [list(map(int, input().split())) for _ in range(self.n)]
        self.match = [-1 for _ in range(self.m)]
        self.adj = [[] for _ in range(self.n)]
        self.get_graph(edges)

        self.count = 0
        for v in range(self.n):
            used = [False for _ in range(self.n)]
            if self.dfs(v, used):
                self.count += 1

        print(self.count)

        for idx, value in enumerate(self.match):
            if value != -1:
                print(value+1, idx+1)

    def dfs(self, v, used):
        if used[v]:
            return False
        used[v] = True

        for u in self.adj[v]:
            if self.match[u - 1] == -1:
                self.match[u - 1] = v
                return True
            if self.dfs(self.match[u - 1], used):
                self.match[u - 1] = v
                return True
        return False

    def get_graph(self, edges):
        for idx, edge in enumerate(edges):
            if edge[0] == 0:
                continue
            else:
                self.adj[idx] = edge[:-1]


Solution()
