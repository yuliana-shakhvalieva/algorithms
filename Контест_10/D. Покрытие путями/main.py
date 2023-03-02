class Solution:
    def __init__(self):
        self.n, self.m = map(int, input().split())
        edges = [list(map(int, input().split())) for _ in range(self.m)]
        self.adj = [[] for _ in range(self.n)]
        self.get_graph(edges)

        self.match = [-1 for _ in range(self.n)]

        self.count = 0
        for v in range(self.n):

            used = [False for _ in range(self.n)]
            if self.dfs(v, used):
                self.count += 1

        self.set_v = set()
        self.v_in_matching = []
        for idx, value in enumerate(self.match):
            if value != -1:
                self.v_in_matching.append(value + 1)
                self.v_in_matching.append(idx + 1)

        count_path = int((2 * len(set(self.v_in_matching)) - len(self.v_in_matching)) / 2)

        print(self.n - len(set(self.v_in_matching)) + count_path)

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
