#python3
import sys


def compute_min_refills(distance, tank, n, stops):
    stops.sort()
    stops = [0] + stops + [distance]
    refills, lastStop, currentPosition = 0, 0, 0
    while currentPosition < n + 1:
        if stops[currentPosition + 1] - stops[lastStop] > tank:
            return -1
        currentPosition += 1
        while (currentPosition < n + 1) and (stops[currentPosition + 1] - stops[lastStop] <= tank):
            currentPosition += 1
        if currentPosition < n + 1:
            refills += 1
            lastStop = currentPosition
    return refills


if __name__ == '__main__':
    d, m, n, *stops = map(int, sys.stdin.read().strip().split())
    print(compute_min_refills(d, m, n, stops))
