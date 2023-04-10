import random


class Node:
    def __init__(self, key, left=None, right=None, size=1):
        self.left = left
        self.right = right
        self.key = key
        self.y = random.random()
        self.size = size


class Solution:
    def __init__(self):
        n, m = map(int, input().split())
        self.tree = None
        self.answer = []

        for i in range(n):
            self.tree = self.add(self.tree, i + 1)

        for _ in range(m):
            l, r = map(int, input().split())
            t1, t2 = self.split(self.tree, r)
            t3, t4 = self.split(t1, l - 1)
            self.tree = self.merge(self.merge(t4, t3), t2)

        self.get_answer(self.tree)
        print(*self.answer)

    def get_answer(self, tree):
        if tree is None:
            return
        self.get_answer(tree.left)
        self.answer.append(tree.key)
        self.get_answer(tree.right)

    def size(self, tree):
        if not tree:
            return 0
        return tree.size

    def update_size(self, tree):
        if tree:
            tree.size = 1 + self.size(tree.left) + self.size(tree.right)

    def add(self, tree, value):
        left_tree, right_tree = self.split(tree, value)
        tree = self.merge(self.merge(left_tree, Node(value)), right_tree)
        return tree

    def merge(self, left_tree, right_tree):
        if not left_tree:
            self.update_size(right_tree)
            return right_tree

        if not right_tree:
            self.update_size(left_tree)
            return left_tree

        if left_tree.y > right_tree.y:
            left_tree.right = self.merge(left_tree.right, right_tree)
            self.update_size(left_tree)
            return left_tree
        else:
            right_tree.left = self.merge(left_tree, right_tree.left)
            self.update_size(right_tree)
            return right_tree

    def split(self, tree, value):
        if tree is None:
            return None, None

        left_size = self.size(tree.left)

        if left_size < value:
            left_tree, right_tree = self.split(tree.right, value - left_size - 1)
            tree.right = left_tree
            self.update_size(tree)
            self.update_size(right_tree)
            return tree, right_tree
        else:
            left_tree, right_tree = self.split(tree.left, value)
            tree.left = right_tree
            self.update_size(tree)
            self.update_size(left_tree)
            return left_tree, tree


Solution()
