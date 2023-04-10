import math


class Solution:
    def __init__(self):
        n, k = map(int, input().split())

        self.modif = [-1 for _ in range(4 * n)]
        self.tree = [math.inf for _ in range(4 * n)]
        self.depth = [0 for _ in range(4 * n)]
        self.built_zero_tree(0, 0, n)

        for i in range(k):
            request = input()
            if request[0] == 'A':
                l, r, value = map(int, request[1:].split())
                self.assign(0, 0, n, l - 1, r, value)
            elif request[0] == 'Q':
                l, r = map(int, request[1:].split())
                print(self.get(0, 0, n, l - 1, r))

    def built_zero_tree(self, node, node_l, node_r):
        if node_l + 1 == node_r:
            self.tree[node] = 0
            self.depth[node] = 1
            return

        mid = node_l + (node_r - node_l) // 2

        self.built_zero_tree(node * 2 + 1, node_l, mid)
        self.built_zero_tree(node * 2 + 2, mid, node_r)
        self.tree[node] = 0
        self.depth[node] = self.depth[node * 2 + 1] + self.depth[node * 2 + 2]

    def push(self, node, node_l, node_r):
        if self.modif[node] == -1:
            return

        self.tree[node] = self.modif[node] * self.depth[node]
        if node_l != node_r - 1:
            self.modif[2 * node + 1] = self.modif[2 * node + 2] = self.modif[node]
        self.modif[node] = -1

    def assign(self, node, node_l, node_r, l, r, value):
        self.push(node, node_l, node_r)

        if l <= node_l and node_r <= r:
            self.modif[node] = value
            return

        if node_r <= l or r <= node_l:
            return

        mid = node_l + (node_r - node_l) // 2

        self.assign(2 * node + 1, node_l, mid, l, r, value)
        self.assign(2 * node + 2, mid, node_r, l, r, value)

        self.tree[node] = 0

        for ch in [2 * node + 1, 2 * node + 2]:
            if self.modif[ch] != -1:
                child = self.modif[ch] * self.depth[ch]
            else:
                child = self.tree[ch]

            self.tree[node] += child

    def get(self, node, node_l, node_r, l, r):
        self.push(node, node_l, node_r)

        if l <= node_l and node_r <= r:
            return self.tree[node]

        if node_r <= l or r <= node_l:
            return 0

        mid = node_l + (node_r - node_l) // 2

        return self.get(2 * node + 1, node_l, mid, l, r) + self.get(2 * node + 2, mid, node_r, l, r)

Solution()
