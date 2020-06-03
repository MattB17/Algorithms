#python3
from random import randint


def PolyHash(s, p, x):
    hash = 0
    for i in range(len(s) - 1, -1, -1):
        hash = ((hash * x) + ord(s[i])) % p
    return hash


def PrecomputeHashes(T, p_len, p, x):
    t_len = len(T)
    H = [None for _ in range(t_len - p_len + 1)]
    H[t_len - p_len] = PolyHash(T[(t_len - p_len):], p, x)
    y = 1
    for i in range(p_len):
        y = (y * x) % p
    for i in range(t_len - p_len - 1, -1, -1):
        H[i] = ((x*H[i + 1]) + ord(T[i]) - (y*ord(T[i + p_len]))) % p
    return H


def RabinKarp(T, P):
    p_len = len(P)
    p = 10**9 + 7
    x = randint(1, p-1)
    result = []
    pHash = PolyHash(P, p, x)
    H = PrecomputeHashes(T, p_len, p, x)
    for i in range(len(H)):
        if pHash != H[i]:
            continue
        if T[i:(i+p_len)] == P:
            result.append(str(i))
    return result


if __name__ == '__main__':
    P = input().strip()
    T = input().strip()
    print(" ".join(RabinKarp(T, P)))
