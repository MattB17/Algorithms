#python3
import sys


def get_change(m):
    denominations = [10, 5, 1]
    coin_count = 0
    for d in denominations:
        coin_count += int(m / d)
        m = m % d
    return coin_count


if __name__ == '__main__':
    m = int(sys.stdin.read().strip())
    print(get_change(m))
