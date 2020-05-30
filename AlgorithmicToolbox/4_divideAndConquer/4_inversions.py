#python3
import sys
import math
import copy


def combine(a, left, right, mid):
    b = copy.deepcopy(a[left:mid])
    c = copy.deepcopy(a[mid:right])
    count = 0
    ptr_a, ptr_b, ptr_c = left, 0, 0
    while (ptr_b < mid - left) and (ptr_c < right - mid):
        if b[ptr_b] <= c[ptr_c]:
            a[ptr_a] = b[ptr_b]
            ptr_b += 1
            count += ptr_c
        else:
            a[ptr_a] = c[ptr_c]
            ptr_c += 1
        ptr_a +=1
    while ptr_b < mid - left:
        a[ptr_a] = b[ptr_b]
        ptr_a += 1
        ptr_b += 1
        count += ptr_c
    while ptr_c < right - mid:
        a[ptr_a] = c[ptr_c]
        ptr_a += 1
        ptr_c += 1
    return count



def get_number_of_inversions(a, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    mid = math.floor((left + right) / 2)
    number_of_inversions += get_number_of_inversions(a, left, mid)
    number_of_inversions += get_number_of_inversions(a, mid, right)
    number_of_inversions += combine(a, left, right, mid)
    return number_of_inversions



if __name__ == '__main__':
    n, *a = list(map(int, sys.stdin.read().split()))
    print(get_number_of_inversions(a, 0, n))
