#python3
import sys
import math


def partition3(a, l, r):
    """We initially keep a[m1] to a[m2] having all values
    equal to num, we have a[m2+1] to a[j] having all values
    less than num, and a[j+1] to a[i] has all values greater
    than num.

    Note for the a[i]==num case:
        we have a[i] == num and then increment j and m2.
        So now a[m2] < num and a[j] > num. So we set
        a[m2] = a[i], a[j] = a[m2], and a[i] = a[j]

    """
    num = a[l]
    m1, m2 = l, l
    i = l + 1
    while i <= r:
        if a[i] < num:
            m2 += 1
            a[i], a[m2], a[m1] = a[m2], a[m1], a[i]
            m1 += 1
        elif a[i] == num:
            m2 += 1
            a[i], a[m2] = a[m2], a[i]
        i += 1
    return m1, m2


def move_pivot(a, l, r):
    k = math.floor(((r - l) / 2) + l)
    if (a[l] <= a[k] <= a[r]) or (a[r] <= a[k] <= a[l]):
        a[l], a[k] = a[k], a[l]
    elif (a[k] <= a[r] <= a[l]) or (a[l] <= a[r] <= a[k]):
        a[l], a[r] = a[r], a[l]


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    while l < r:
        move_pivot(a, l, r)
        m1, m2 = partition3(a, l, r)
        if (m1 - l) < (r - m2):
            randomized_quick_sort(a, l, m1 - 1)
            l = m2 + 1
        else:
            randomized_quick_sort(a, m2 + 1, r)
            r = m1 - 1


if __name__ == '__main__':
    n = int(input().strip())
    a = [int(x) for x in input().strip().split()]
    randomized_quick_sort(a, 0, n-1)
    for x in a:
        print(x, end=' ')
