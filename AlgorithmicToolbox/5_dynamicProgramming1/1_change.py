#python3
import sys


denominations = [1, 3, 4]


def get_change(m):
    change_count = [0 for _ in range(m + 1)]
    for i in range(1, m + 1):
        change_count[i] = change_count[i - 1] + 1
        for coin in denominations[1:]:
            if coin <= i:
                numCoins = change_count[(i-coin)] + 1
                change_count[i] = min(change_count[i], numCoins)
    return change_count[m]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
