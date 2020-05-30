#python3

"""Note that longest common subsequence is just max(n, m) - edit_distance.

"""
import sys


def lcs2(a, n, b, m):
    common_count = [[0 for _ in range(m + 1)]
                    for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            insertion = common_count[i-1][j]
            deletion = common_count[i][j - 1]
            match_mismatch = common_count[i-1][j-1]
            if a[i - 1] == b[j - 1]:
                common_count[i][j] = max(
                    insertion, deletion, match_mismatch + 1)
            else:
                common_count[i][j] = max(
                    insertion, deletion, match_mismatch)
    return common_count[i][j]


if __name__ == '__main__':
    n = int(input().strip())
    a = input().strip().split()
    m = int(input().strip())
    b = input().strip().split()
    print(lcs2(a, n, b, m))
