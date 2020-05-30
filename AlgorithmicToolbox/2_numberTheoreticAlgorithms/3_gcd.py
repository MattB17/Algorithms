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

if __name__ == "__main__":
    a, b = map(int, sys.stdin.read().strip().split())
    print(gcd(a, b))
