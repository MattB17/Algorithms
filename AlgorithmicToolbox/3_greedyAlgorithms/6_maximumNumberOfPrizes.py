#python3
import sys


def optimal_prizes(n):
    prizes = []
    prize_size = 1
    while n > 0:
        if (2 * prize_size) + 1 > n:
            prizes.append(n)
            n = 0
        else:
            prizes.append(prize_size)
            n -= prize_size
            prize_size += 1
    return prizes


if __name__ == '__main__':
    n = int(input().strip())
    prizes = optimal_prizes(n)
    print(len(prizes))
    print(*prizes)
