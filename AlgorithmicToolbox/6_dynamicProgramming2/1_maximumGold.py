#python3
import sys


def optimal_weight(W, n, weights):
    values = [[0 for _ in range(n+1)]
              for _ in range(W+1)]
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            values[w][i] = values[w][i - 1]
            if weights[i - 1] <= w:
                val = values[w - weights[i - 1]][i - 1] + weights[i - 1]
                if values[w][i] < val:
                    values[w][i] = val
    return values[W][n]


if __name__ == '__main__':
    W, n, *weights = list(map(int, sys.stdin.read().split()))
    print(optimal_weight(W, n, weights))
