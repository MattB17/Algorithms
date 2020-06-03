#python3
from random import randint


class Query:
    def __init__(self, query):
        self.a = int(query[0])
        self.b = int(query[1])
        self.l = int(query[2])


def PrecomputeHashes(m, n, x, s):
    H = [None for _ in range(n+1)]
    H[0] = 0
    for i in range(1, n+1):
        H[i] = ((x * H[i-1]) + ord(s[i - 1])) % m
    return H


def check_equalities(queries, q, s, m1, m2):
    n = len(s)
    x = randint(1, 10**9)
    H1 = PrecomputeHashes(m1, n, x, s)
    H2 = PrecomputeHashes(m2, n, x, s)
    result = [None for _ in range(q)]
    for j in range(q):
        query = queries[j]
        result[j] = "No"
        y1 = pow(x, query.l, m1)
        h1_a = (H1[query.a + query.l] - (y1*H1[query.a])) % m1
        h1_b = (H1[query.b + query.l] - (y1*H1[query.b])) % m1
        if (h1_a == h1_b):
            y2 = pow(x, query.l, m2)
            h2_a = (H2[query.a + query.l] - (y2*H2[query.a])) % m2
            h2_b = (H2[query.b + query.l] - (y2*H2[query.b])) % m2
            if (h2_a == h2_b):
                result[j] = "Yes"
    return result


if __name__ == '__main__':
    s = input().strip()
    q = int(input().strip())
    queries = [Query(input().strip().split()) for _ in range(q)]
    query_results = check_equalities(queries, q, s, 10**9 + 7, 10**9 + 9)
    print("\n".join(query_results))
