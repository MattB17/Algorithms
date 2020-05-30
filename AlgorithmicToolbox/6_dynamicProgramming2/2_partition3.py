#python3
import sys


def partition3(arr, n):
    s = sum(arr)
    if s % 3 != 0:
        return 0
    s3 = int(s / 3)
    return has_3_partition(arr, n, (s3, s3, s3))


def has_3_partition(arr, i, p_triple):
    if i == 0:
        return 1 if p_triple == (0, 0, 0) else 0
    p_triple1 = (p_triple[0] - arr[i-1], p_triple[1], p_triple[2])
    p_triple2 = (p_triple[0], p_triple[1] - arr[i-1], p_triple[2])
    p_triple3 = (p_triple[0], p_triple[1], p_triple[2] - arr[i-1])
    if p_triple[0] == p_triple[1] == p_triple[2]:
        return has_3_partition(arr, i-1, p_triple1)
    if (p_triple[0] == p_triple[1]) or (p_triple[1] == p_triple[2]):
        return max(has_3_partition(arr, i-1, p_triple1),
                   has_3_partition(arr, i-1, p_triple3))
    if p_triple[0] == p_triple[2]:
        return max(has_3_partition(arr, i-1, p_triple1),
                   has_3_partition(arr, i-1, p_triple2))
    return max(has_3_partition(arr, i-1, p_triple1),
               has_3_partition(arr, i-1, p_triple2),
               has_3_partition(arr, i-1, p_triple3))



if __name__ == '__main__':
    n = int(input().strip())
    arr = [int(x) for x in input().strip().split()]
    print(partition3(arr, n))
