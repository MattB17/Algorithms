#python3
import sys

def gcd(a, b):
    if b > a:
        return gcd(b, a)
    best = 1
    while True:
        if a % b == 0:
            best = b
            break
        a, b = b, a % b
    return best

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    d = gcd(a, b)
    return int((a / d) * b)

if __name__ == '__main__':
    a, b = [int(x) for x in input().strip().split()]
    print(lcm(a, b))
