#python3
from random import randint
import math
import sys


class Query:
    def __init__(self, query):
        self.k = int(query[0])
        self.text = query[1]
        self.pattern = query[2]


def PrecomputeHashes(m, n, x, s):
    H = [None for _ in range(n+1)]
    H[0] = 0
    for i in range(1, n+1):
        H[i] = ((x * H[i-1]) + ord(s[i - 1])) % m
    return H


def find_next_mismatch(H1_p, H2_p, H1_t, H2_t, x,
                       m1, m2, start, end, text_idx, query):
    low = start
    high = end
    while low <= high - 2:
        t = text_idx + low
        l = math.ceil((high - low) / 2)
        y1 = pow(x, l, m1)
        h1_p = (H1_p[low + l] - (y1*H1_p[low])) % m1
        h1_t = (H1_t[t + l] - (y1*H1_t[t])) % m1
        if (h1_p == h1_t):
            y2 = pow(x, l, m2)
            h2_p = (H2_p[low + l] - (y2*H2_p[low])) % m2
            h2_t = (H2_t[t + l] - (y2*H2_t[t])) % m2
            if (h2_p == h2_t):
                low = low + l
            else:
                high = low + l
        else:
            high = low + l
    if low < high:
        return low + (query.pattern[low] == query.text[text_idx + low])
    return low


def find_fuzzy_matches(query, m1, m2, x):
    p_len = len(query.pattern)
    H1_p = PrecomputeHashes(m1, p_len, x, query.pattern)
    H2_p = PrecomputeHashes(m2, p_len, x, query.pattern)
    t_len = len(query.text)
    H1_t = PrecomputeHashes(m1, t_len, x, query.text)
    H2_t = PrecomputeHashes(m2, t_len, x, query.text)
    fuzzy_matches = []
    for i in range(0, t_len - p_len + 1):
        curr_idx = 0
        mismatches = 0
        while (mismatches <= query.k):
            curr_idx = find_next_mismatch(
                H1_p, H2_p, H1_t, H2_t, x,
                m1, m2, curr_idx, p_len, i, query)
            if curr_idx < p_len:
                mismatches += 1
            else:
                fuzzy_matches.append(i)
                break
            curr_idx += 1
    return fuzzy_matches


if __name__ == '__main__':
    m1 = 10**9 + 7
    m2 = 10**9 + 9
    x = randint(1, 10**9)
    queries = []
    for line in sys.stdin.readlines():
        queries.append(Query(line.strip().split()))
    for query in queries:
        result = find_fuzzy_matches(query, m1, m2, x)
        n = len(result)
        if n == 0:
            print(n)
        else:
            print(n, end=" ")
            print(" ".join([str(x) for x in result]))
