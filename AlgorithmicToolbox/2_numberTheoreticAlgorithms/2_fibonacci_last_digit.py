#python3
import sys

def get_fibonacci_last_digit(n):
    if n <= 1:
        return n
    prev2 = 0
    prev = 1
    for _ in range(2, n):
        new_digit = (prev + prev2) % 10
        prev2 = prev
        prev = new_digit
    return (prev + prev2) % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
