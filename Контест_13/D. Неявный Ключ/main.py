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
        array = list(map(int, input().split()))
        self.tree = None
        self.answer = []

        for i in range(n):
            self.tree = self.add_idx(self.tree, i, array[i])

        for i in range(m):
            request = input()
            if request[:3] == 'del':
                j = int(request[4:])
                self.tree = self.delete(self.tree, j - 1)

            elif request[:3] == 'add':
                j, value = map(int, request[4:].split())
                self.tree = self.add_idx(self.tree, j, value)

        self.get_answer(self.tree)
        print(self.size(self.tree))
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

    def add_idx(self, tree, index, value):
        left_tree, right_tree = self.split(tree, index)
        tree = self.merge(self.merge(left_tree, Node(value)), right_tree)
        return tree

    def delete(self, tree, index):
        t1, t2 = self.split(tree, index)
        t3, t4 = self.split(t2, 1)
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

    def split(self, tree, index):
        if tree is None:
            return None, None

        left_size = self.size(tree.left)

        if left_size < index:
            left_tree, right_tree = self.split(tree.right, index - left_size - 1)
            tree.right = left_tree
            self.update_size(tree)
            self.update_size(right_tree)
            return tree, right_tree
        else:
            left_tree, right_tree = self.split(tree.left, index)
            tree.left = right_tree
            self.update_size(tree)
            self.update_size(left_tree)
            return left_tree, tree


Solution()
