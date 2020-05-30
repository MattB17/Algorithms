#python3
import sys
import math


def compute_distance(pointA, pointB):
    x_diff = pointA[0] - pointB[0]
    y_diff = pointA[1] - pointB[1]
    return math.sqrt(x_diff**2 + y_diff**2)


def compute_sorted_distances(sorted_arr, x_val, distance):
    filtered = [point for point in sorted_arr
                if -distance <= point[0] - x_val <= distance]
    l = len(filtered)
    min_distance = distance
    for i in range(l-1):
        for j in range(i+1, min(i+7, l)):
            new_distance = compute_distance(filtered[i], filtered[j])
            if new_distance < min_distance:
                min_distance = new_distance
    return min_distance


def minimum_distance(sorted_by_x, sorted_by_y):
    n = len(sorted_by_x)
    if n <= 3:
        return brute_force(sorted_by_x)
    m = math.floor(n / 2)
    lower_half = sorted_by_x[:m]
    upper_half = sorted_by_x[m:]
    mid_x = upper_half[0][0]
    lower_half_y = [point for point in sorted_by_y if point[0] <= mid_x]
    upper_half_y = [point for point in sorted_by_y if point[0] > mid_x]
    d1 = min(minimum_distance(lower_half, lower_half_y),
             minimum_distance(upper_half, upper_half_y))
    return min(d1, compute_sorted_distances(sorted_by_y, mid_x, d1))


def brute_force(arr_x):
    min_dist = compute_distance(arr_x[0], arr_x[1])
    l = len(arr_x)
    if l <= 2:
        return min_dist
    for i in range(l - 1):
        for j in range(i+1, l):
            dist = compute_distance(arr_x[i], arr_x[j])
            if dist < min_dist:
                min_dist = dist
    return min_dist


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    lst = list(zip(x, y))
    sorted_x = sorted(lst, key=lambda point: point[0])
    sorted_y = sorted(lst, key=lambda point: point[1])
    print("{0:.9f}".format(minimum_distance(sorted_x, sorted_y)))
