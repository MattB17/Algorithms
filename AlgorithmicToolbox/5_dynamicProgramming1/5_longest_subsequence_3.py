#python3
import sys


def lcs3(a, n, b, m, c, l):
    common_count = [[[0 for _ in range(l + 1)]
                     for _ in range(m + 1)]
                    for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            for k in range(1, l + 1):
                indel = max(
                    common_count[i][j][k-1], common_count[i][j-1][k],
                    common_count[i-1][j][k], common_count[i][j-1][k-1],
                    common_count[i-1][j][k-1], common_count[i-1][j-1][k])
                match_mismatch = common_count[i-1][j-1][k - 1]
                if a[i - 1] == b[j - 1] == c[k - 1]:
                    common_count[i][j][k] = max(indel, match_mismatch + 1)
                else:
                    common_count[i][j][k] = max(indel, match_mismatch)
    return common_count[n][m][l]


if __name__ == '__main__':
    n = int(input().strip())
    a = input().strip().split()
    m = int(input().strip())
    b = input().strip().split()
    l = int(input().strip())
    c = input().strip().split()
    print(lcs3(a, n, b, m, c, l))
