#python3
import sys


def get_optimal_sequence(n):
    operations = lowest_operations(n)
    operations_count = operations[n-1] + 1
    sequence = [1 for _ in range(operations_count)]
    while n > 1:
        sequence[operations_count - 1] = n
        if operations[n-1] == operations[n - 2] + 1:
            n = n - 1
        elif (n % 2 == 0) and (operations[n - 1] == operations[int(n / 2) - 1] + 1):
            n = int(n / 2)
        else:
            n = int(n / 3)
        operations_count -= 1
    return sequence



def lowest_operations(n):
    operation_count = [0 for _ in range(n)]
    for i in range(2, n + 1):
        operation_count[i - 1] = operation_count[i - 2] + 1
        if i % 2 == 0:
            operation_count[i-1] = min(
                operation_count[i - 1], operation_count[int(i / 2) - 1] + 1)
        if i % 3 == 0:
            operation_count[i - 1] = min(
                operation_count[i - 1], operation_count[int(i / 3) - 1] + 1)
    return operation_count


if __name__ == '__main__':
    n = int(sys.stdin.read().strip())
    optimal_sequence = get_optimal_sequence(n)
    print(len(optimal_sequence) - 1)
    for x in optimal_sequence:
        print(x, end=' ')
