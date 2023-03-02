class Solution:
    def __init__(self):
        self.p = 5
        self.M = 10 ** 18 + 3
        self.string, self.q, self.requests = self.read_data()
        self.int_from_str = list()
        self.pows = [1]
        self.hash_prefix = [0]

    def read_data(self):
        string = input()
        q = int(input())
        requests = [list(map(int, input().split())) for _ in range(q)]

        return string, q, requests

    def pre_calculation(self):
        for i in range(1, len(self.string) + 1):
            self.pows.append((self.p * self.pows[i - 1]) % self.M)
            self.hash_prefix.append((self.p * self.hash_prefix[i - 1] + ord(self.string[i - 1])) % self.M)

    def hash_substring(self, l, r):
        return (self.hash_prefix[r] - self.hash_prefix[l-1] * self.pows[r + 1 - l]) % self.M

    def check(self, request):
        l_1, r_1, l_2, r_2 = request
        if self.hash_substring(l_1, r_1) == self.hash_substring(l_2, r_2):
            return '+'
        else:
            return '-'

    def get_solution(self):
        self.pre_calculation()
        return [self.check(request) for request in self.requests]


result = Solution().get_solution()
print(*result, sep='')



