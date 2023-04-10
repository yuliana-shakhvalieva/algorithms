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
        n = int(input())
        self.tree = None
        self.count = 0

        for i in range(n):
            c, k = map(int, input().split())
            if c == 1:
                self.tree = self.add(self.tree, k)
                self.count += 1
            elif c == 0:
                print(self.find_k_max(self.tree, self.count - k))
            elif c == -1:
                self.tree = self.delete(self.tree, k)
                self.count -= 1

    def find_k_max(self, tree, k):
        left_size = self.size(tree.left)
        if left_size == k:
            return tree.key
        elif left_size > k:
            return self.find_k_max(tree.left, k)
        else:
            k -= left_size + 1
            return self.find_k_max(tree.right, k)

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

    def delete(self, tree, value):
        t1, t2 = self.split(tree, value)
        t3, t4 = self.split(t2, value + 1)
        return self.merge(t1, t4)

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

        if tree.key < value:
            left_tree, right_tree = self.split(tree.right, value)
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
