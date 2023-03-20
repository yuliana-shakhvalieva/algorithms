import math
from sys import stdin


class Solution:
    def __init__(self):
        n = int(input())
        self.array = list(map(int, input().split()))
        self.tree = [math.inf for _ in range(4*n)]
        self.get_min_tree(0, 0, n)

        for line in stdin:
            operation, a, b = list(map(str, line.rstrip().split()))
            a, b = int(a), int(b)

            if operation == 'min':
                print(self.get(0, 0, n, a - 1, b))
            elif operation == 'set':
                self.update(0, 0, n, a - 1, b)

    def get_min_tree(self, node, node_l, node_r):
        if node_l + 1 == node_r:
            self.tree[node] = self.array[node_l]
            return

        mid = node_l + (node_r - node_l) // 2

        self.get_min_tree(node * 2 + 1, node_l, mid)
        self.get_min_tree(node * 2 + 2, mid, node_r)
        self.tree[node] = min(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def get(self, node, node_l, node_r, l, r):
        if l <= node_l and node_r <= r:
            return self.tree[node]

        if node_r <= l or r <= node_l:
            return math.inf

        mid = node_l + (node_r - node_l) // 2

        return min(self.get(2 * node + 1, node_l, mid, l, r),
                   self.get(2 * node + 2, mid, node_r, l, r))

    def update(self, node, node_l, node_r, i, new_value):
        if node_r == node_l + 1:
            assert i == node_l
            self.tree[node] = new_value
            return

        mid = node_l + (node_r - node_l) // 2

        if i < mid:
            self.update(2 * node + 1, node_l, mid, i, new_value)
        else:
            self.update(2 * node + 2, mid, node_r, i, new_value)

        self.tree[node] = min(self.tree[2 * node + 1],
                              self.tree[2 * node + 2])


Solution()
