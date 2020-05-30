#python3
import sys


def get_intervals_below(point, upper_points, left, right):
    if right - left <= 1:
        return left + (upper_points[left] < point)
    m = (left + right) // 2
    if upper_points[m] >= point:
        return get_intervals_below(point, upper_points, left, m)
    return get_intervals_below(point, upper_points, m, right)


def get_intervals_above(point, lower_points, left, right):
    if right - left <= 1:
        return left + (lower_points[left] <= point)
    m = (left + right) // 2
    if lower_points[m] > point:
        return get_intervals_above(point, lower_points, left, m)
    return get_intervals_above(point, lower_points, m, right)


def count_interval(point, x_list, y_list, s):
    invalid_x = s - get_intervals_above(point, x_list, 0, s)
    invalid_y = get_intervals_below(point, y_list, 0, s)
    return s - invalid_x - invalid_y


if __name__ == '__main__':
    s, p = [int(x) for x in input().strip().split()]
    x_lst = [None for _ in range(s)]
    y_lst = [None for _ in range(s)]
    for i in range(s):
        x, y = [int(x) for x in input().strip().split()]
        x_lst[i] = x
        y_lst[i] = y
    x_lst.sort()
    y_lst.sort()
    for point in input().strip().split():
        print(count_interval(int(point), x_lst, y_lst, s), end=" ")
