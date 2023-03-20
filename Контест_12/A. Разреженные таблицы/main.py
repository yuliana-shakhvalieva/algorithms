import math


class Solution:
    def __init__(self):
        self.n, self.m, self.a_1 = map(int, input().split())
        self.l, self.r = map(int, input().split())
        self.a_i_1 = self.a_1
        self.k = self.pre_calc_k()
        self.f = self.pre_calc_f()
        self.ans_i_1 = self.get(self.l, self.r)
        print(*self.last_get())

    def last_get(self):
        for i in range(1, self.m):
            self.upload_l_r(i)
            self.ans_i_1 = self.get(self.l, self.r)

        return self.l, self.r, self.ans_i_1

    def upload_l_r(self, i):
        self.l = ((17 * self.l + 751 + self.ans_i_1 + 2 * i) % self.n) + 1
        self.r = ((13 * self.r + 593 + self.ans_i_1 + 5 * i) % self.n) + 1

    def pre_calc_k(self):
        k = [0 for _ in range(self.n + 1)]
        k[1] = 0
        for i in range(2, self.n + 1):
            k[i] = 1 + k[math.floor(i / 2)]
        return k

    def pre_calc_f(self):
        f = [[math.inf for _ in range(self.n)] for _ in range(self.k[-1] + 1)]

        f[0][0] = self.a_1
        for i in range(1, self.n):
            f[0][i] = self.get_a_i()

        for k in range(1, self.k[-1] + 1):
            for i in range(self.n - 2 ** k + 1):
                f[k][i] = min(f[k - 1][i], f[k - 1][i + 2 ** (k - 1)])

        return f

    def get_a_i(self):
        a_i = (23 * self.a_i_1 + 21563) % 16714589
        self.a_i_1 = a_i
        return a_i

    def get(self, l, r):
        if l > r:
            l, r = r, l
        k = self.k[r - l]
        return min(self.f[k][l - 1], self.f[k][r - 2 ** k])


Solution()
