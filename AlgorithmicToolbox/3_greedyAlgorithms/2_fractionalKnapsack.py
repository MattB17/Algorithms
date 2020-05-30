#python3
import sys


def get_optimal_val(capacity, weights, values):
    value = 0.
    item_pairs = [(values[i], weights[i]) for i in range(len(weights))]
    item_pairs.sort(key=lambda item_pair: -(item_pair[0]/item_pair[1]))
    for i in range(n):
        if capacity == 0:
            return value
        a = min(item_pairs[i][1], capacity)
        value += (a * (item_pairs[i][0]/item_pairs[i][1]))
        capacity -= a
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_val = get_optimal_val(capacity, weights, values)
    print("{:.10f}".format(opt_val))
