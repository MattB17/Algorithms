#python3
import sys

def pisanoPeriod(m):
    period = [0, 1]
    while True:
        period.append((period[-1] + period[-2]) % m)
        if period[-1] == 1 and period[-2] == 0:
            return period[:-2]


def fib_sum(n):
    if n <= 1:
        return n
    period = pisanoPeriod(10)
    l = len(period)
    d = int(n / l)
    s = (sum(period[:(n % l) + 1]) * (d + 1)) + (sum(period[(n % l) + 1:]) * d)
    return s % 10


def fib_partial(n, m):
    if m == 0:
        return fib_sum(n)
    return (fib_sum(n) - fib_sum(m-1)) % 10


if __name__ == '__main__':
    m, n = map(int, sys.stdin.read().strip().split())
    print(fib_partial(n, m))
