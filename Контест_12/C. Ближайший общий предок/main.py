import math


class Solution:
    def __init__(self):
        n = int(input())
        parents = list(map(int, input().split()))
        self.root = None
        self.adj = self.get_adj(n, parents)
        self.used = [False for _ in range(n)]
        self.ind = []
        self.dfs(self.root, 0)

        self.tree = [math.inf for _ in range(4 * len(self.ind))]
        self.built_min_tree(0, 0, len(self.ind))

        m = int(input())
        for i in range(m):
            a, b = map(int, input().split())
            found_a = False
            found_b = False
            j = 0
            while not found_a or not found_b:
                if not found_a and self.ind[j][0] == a - 1:
                    found_a = True
                    ind_a = j
                if not found_b and self.ind[j][0] == b - 1:
                    found_b = True
                    ind_b = j
                j += 1

            if ind_a > ind_b:
                ind_a, ind_b = ind_b, ind_a

            v = self.get(0, 0, len(self.ind), ind_a, ind_b + 1)[0]
            print(v + 1)

    def dfs(self, v, depth):
        self.ind.append((v, depth))
        self.used[v] = True

        for u in self.adj[v]:
            if not self.used[u]:
                self.dfs(u, depth + 1)
                self.ind.append((v, depth))

    def get_adj(self, n, parents):
        adj = [[] for _ in range(n)]
        for i in range(n):
            parent = parents[i] - 1
            if parent != -1:
                adj[i].append(parent)
                adj[parent].append(i)
            else:
                self.root = i
        return adj

    def built_min_tree(self, node, node_l, node_r):
        if node_l + 1 == node_r:
            self.tree[node] = self.ind[node_l]
            return

        mid = node_l + (node_r - node_l) // 2

        self.built_min_tree(node * 2 + 1, node_l, mid)
        self.built_min_tree(node * 2 + 2, mid, node_r)
        if self.tree[2 * node + 1][1] < self.tree[2 * node + 2][1]:
            self.tree[node] = self.tree[2 * node + 1]
        else:
            self.tree[node] = self.tree[2 * node + 2]

    def get(self, node, node_l, node_r, l, r):
        if l <= node_l and node_r <= r:
            return self.tree[node]

        if node_r <= l or r <= node_l:
            return math.inf, math.inf

        mid = node_l + (node_r - node_l) // 2

        a = self.get(2 * node + 1, node_l, mid, l, r)
        b = self.get(2 * node + 2, mid, node_r, l, r)

        if a[1] < b[1]:
            return a
        else:
            return b


Solution()
