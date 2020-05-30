#python3
def calc_fib(n):
    if n <= 1:
        return n
    prev = 1
    prev2 = 0
    for _ in range(2, n):
        prev2, prev = prev, prev2 + prev
    return prev + prev2

n = int(input())
print(calc_fib(n))
