#python3
import sys


def max_dot_product(a, b, n):
    a.sort()
    b.sort()
    return sum([a[i]*b[i]
               for i in range(n)])


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    a = data[1:(n+1)]
    b = data[(n+1):]
    print(max_dot_product(a, b, n))
