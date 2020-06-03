#python3
import math
from random import randint
import sys


def PrecomputeHashes(m, n, x, s):
    H = [None for _ in range(n+1)]
    H[0] = 0
    for i in range(1, n+1):
        H[i] = ((x * H[i-1]) + ord(s[i - 1])) % m
    return H



class IndexHash:
    def __init__(self):
        self.table = {}

    def add(self, pre_hash, idx):
        self.table[pre_hash] = idx

    def has_value_at_hash(self, pre_hash):
        return pre_hash in self.table

    def get_idx_at_hash(self, pre_hash):
        return self.table[pre_hash]


class PreHash:
    def __init__(self, m, x, text, n):
        self.text = text
        self.x = x
        self.m = m
        self.n = n
        self.table = PrecomputeHashes(m, n, x, text)

    def get_x_factor(self, l):
        return pow(self.x, l, self.m)

    def get_pre_hash(self, idx, l, x_factor):
        return (self.table[idx + l] - (x_factor * self.table[idx])) % self.m


def find_common_substring(pre_hash_s1, pre_hash_s2,
                          pre_hash_t1, pre_hash_t2, k):
    s_hash1 = IndexHash()
    s_hash2 = IndexHash()
    x_factor1 = pre_hash_s1.get_x_factor(k)
    x_factor2 = pre_hash_s2.get_x_factor(k)
    for i in range(0, pre_hash_s1.n - k + 1):
        pre_hash1 = pre_hash_s1.get_pre_hash(i, k, x_factor1)
        pre_hash2 = pre_hash_s2.get_pre_hash(i, k, x_factor2)
        s_hash1.add(pre_hash1, i)
        s_hash2.add(pre_hash2, i)
    x_factor1 = pre_hash_t1.get_x_factor(k)
    x_factor2 = pre_hash_t2.get_x_factor(k)
    for i in range(0, pre_hash_t1.n - k + 1):
        pre_hash1 = pre_hash_t1.get_pre_hash(i, k, x_factor1)
        if s_hash1.has_value_at_hash(pre_hash1):
            pre_hash2 = pre_hash_t2.get_pre_hash(i, k, x_factor2)
            if s_hash2.has_value_at_hash(pre_hash2):
                return (s_hash2.get_idx_at_hash(pre_hash2), i, k)
    return None


def search_for_lcs(s, t, m1, m2, x):
    len_s = len(s)
    len_t = len(t)
    pre_hash_s1 = PreHash(m1, x, s, len_s)
    pre_hash_s2 = PreHash(m2, x, s, len_s)
    pre_hash_t1 = PreHash(m1, x, t, len_t)
    pre_hash_t2 = PreHash(m2, x, t, len_t)
    best = (0, 0, 0)
    low = 1
    high = min(len_s, len_t)
    while low <= high:
        mid = math.floor((low + high) / 2)
        result = find_common_substring(
            pre_hash_s1, pre_hash_s2, pre_hash_t1, pre_hash_t2, mid)
        if result is None:
            high = mid - 1
        else:
            best = result
            low = mid + 1
    return best


if __name__ == '__main__':
    m1 = 1000000007
    m2 = 1000004249
    x = randint(1, 1000000007)
    results = []
    for line in sys.stdin.readlines():
        s, t = line.strip().split()
        results.append(search_for_lcs(s, t, m1, m2, x))
    for result in results:
        print("{0} {1} {2}".format(result[0], result[1], result[2]))
