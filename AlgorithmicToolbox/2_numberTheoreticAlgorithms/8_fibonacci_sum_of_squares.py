#python3
import sys


def pisanoPeriod(m):
    period = [0, 1]
    while True:
        period.append((period[-1] + period[-2]) % m)
        if period[-1] == 1 and period[-2] == 0:
            return period[:-2]


def fib_sum_of_squares(n):
    period = pisanoPeriod(10)
    l = len(period)
    width = period[n % l]
    length = period[(n+1) % l]
    return (length * width) % 10


if __name__ == '__main__':
    n = int(sys.stdin.read().strip())
    print(fib_sum_of_squares(n))
