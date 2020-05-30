#python3
import sys


def has_majority_element(a, n):
    num_counts = {}
    for num in a:
        if num in num_counts:
            num_counts[num] += 1
        else:
            num_counts[num] = 1
    for num, count in num_counts.items():
        if count > (n / 2):
            return 1
    return 0


if __name__ == '__main__':
    n, *a = list(map(int, sys.stdin.read().split()))
    print(has_majority_element(a, n))
