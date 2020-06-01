#python3
import math


def left_child(i):
    return 2*i + 1


def right_child(i):
    return 2*i + 2


def parent(i):
    return math.floor((i - 1) / 2)


def sift_down(arr, i, n, swaps):
    curr_idx = i
    less_than_children = False
    while (not less_than_children) and curr_idx < n:
        min_idx = curr_idx
        l = left_child(curr_idx)
        if l < n and arr[l] < arr[min_idx]:
            min_idx = l
        r = right_child(curr_idx)
        if r < n and arr[r] < arr[min_idx]:
            min_idx = r
        if curr_idx != min_idx:
            arr[curr_idx], arr[min_idx] = arr[min_idx], arr[curr_idx]
            swaps.append((curr_idx, min_idx))
            curr_idx = min_idx
        else:
            less_than_children = True


def make_heap(arr, n):
    swaps = []
    largest_internal_idx = math.floor((n-1) / 2)
    for i in range(largest_internal_idx, -1, -1):
        sift_down(arr, i, n, swaps)
    return swaps



if __name__ == '__main__':
    n = int(input().strip())
    data = [int(x) for x in input().strip().split()]
    swaps = make_heap(data, n)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
