#python3
import sys
import math


def binary_search(a, num):
    left, right = 0, len(a) - 1
    while left <= right:
        m = math.floor(((right - left) / 2) + left)
        if a[m] == num:
            return m
        if a[m] > num:
            right = m - 1
        else:
            left = m + 1
    return -1


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1: n+1]
    for num in data[n+2:]:
        print(binary_search(a, num), end=' ')
