class Solution:
    def __init__(self):
        self.p = 27
        self.M = 10 ** 18 + 3
        self.n, self.string_1, self.string_2 = self.read_data()
        self.pows = [1]
        self.hash_prefix_1 = [ord(self.string_1[0]) % self.M]
        self.hash_prefix_2 = [ord(self.string_2[0]) % self.M]
        self.index = None

    def read_data(self):
        n = int(input())
        string_1 = input()
        string_2 = input()
        return n, string_1, string_2

    def pre_calculation(self):
        for i in range(1, self.n):
            self.pows.append((self.p * self.pows[i - 1]) % self.M)
            self.hash_prefix_1.append((self.p * self.hash_prefix_1[i - 1] + ord(self.string_1[i])) % self.M)
            self.hash_prefix_2.append((self.p * self.hash_prefix_2[i - 1] + ord(self.string_2[i])) % self.M)

    def count_hash_substring(self, hash_prefix, l, r):
        return (hash_prefix[r] - hash_prefix[l - 1] * self.pows[r + 1 - l]) % self.M

    def count_hash_length_k_string_1(self, k):
        hash = [self.hash_prefix_1[k - 1]]
        for i in range(1, self.n - k + 1):
            hash.append(self.count_hash_substring(self.hash_prefix_1, i, i + k - 1))
        return hash

    def binary_search(self, array, x):
        left = -1
        right = len(array)

        while right - left != 1:
            mid = (right + left) // 2
            if array[mid] == x:
                return True
            if array[mid] > x:
                right = mid
            else:
                left = mid
        return False

    def idx_common_substring_length_k(self, k):
        hash_k_string_1 = self.count_hash_length_k_string_1(k)
        hash_k_string_1 = sorted(hash_k_string_1)

        if self.binary_search(hash_k_string_1, self.hash_prefix_2[k - 1]):
            return 0

        for i in range(1, self.n - k + 1):
            if self.binary_search(hash_k_string_1, self.count_hash_substring(self.hash_prefix_2, i, i + k - 1)):
                return i
            
        return -1

    def get_max_common_substring(self):
        left = 0
        right = self.n + 1

        while right - left > 1:
            k = (right + left) // 2
            idx = self.idx_common_substring_length_k(k)
            if idx != -1:
                left = k
                self.index = idx
            else:
                right = k

        return self.index, left

    def get_solution(self):
        self.pre_calculation()
        idx, k = self.get_max_common_substring()
        return self.string_2[idx:idx + k]


result = Solution().get_solution()
print(*result, sep='')
