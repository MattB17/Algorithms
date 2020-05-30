#python3
import sys


def edit_distance(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    distances = [[0 for _ in range(l2 + 1)]
                 for _ in range(l1 + 1)]
    for j in range(l2 + 1):
        distances[0][j] = j
    for i in range(l1 + 1):
        distances[i][0] = i
    for i in range(1, l1 + 1):
        for j in range(1, l2 + 1):
            insertion = distances[i-1][j] + 1
            deletion = distances[i][j-1] + 1
            match_mismatch = distances[i-1][j-1]
            if str1[i-1] == str2[j-1]:
                distances[i][j] = min(
                    insertion, deletion, match_mismatch)
            else:
                distances[i][j] = min(
                    insertion, deletion, match_mismatch + 1)
    return distances[l1][l2]


if __name__ == '__main__':
    str1 = input().strip()
    str2 = input().strip()
    print(edit_distance(str1, str2))
