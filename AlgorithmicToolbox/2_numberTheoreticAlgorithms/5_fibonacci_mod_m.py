#python3
import sys


def pisanoPeriod(m):
    period = [0, 1]
    while True:
        period.append((period[-1] + period[-2]) % m)
        if period[-1] == 1 and period[-2] == 0:
            return period[:-2]




def get_fib_mod_m(n, m):
    if n <= 1:
        return n
    period = pisanoPeriod(m)
    return period[n % len(period)]


if __name__ == '__main__':
    n, m = map(int, sys.stdin.read().strip().split())
    print (get_fib_mod_m(n, m))
