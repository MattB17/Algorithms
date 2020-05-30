#python3
import sys
import math

def is_larger_number(x, y):
    a = x + y
    b = y + x
    if a > b:
        return True
    return False


def merge_sorted_digits(digits1, digits2):
    l1 = len(digits1)
    l2 = len(digits2)
    digits = [None for _ in range(l1 + l2)]
    idx = 0
    ptr1 = 0
    ptr2 = 0
    while ptr1 < l1 and ptr2 < l2:
        if is_larger_number(digits1[ptr1], digits2[ptr2]):
            digits[idx] = digits1[ptr1]
            ptr1 += 1
        else:
            digits[idx] = digits2[ptr2]
            ptr2 += 1
        idx += 1
    while ptr1 < l1:
        digits[idx] = digits1[ptr1]
        idx += 1
        ptr1 += 1
    while ptr2 < l2:
        digits[idx] = digits2[ptr2]
        idx += 1
        ptr2 += 1
    return digits



def sort_digits(digits):
    l = len(digits)
    if l <= 1:
        return digits
    m = math.floor(l / 2)
    digits1 = sort_digits(digits[:m])
    digits2 = sort_digits(digits[m:])
    return merge_sorted_digits(digits1, digits2)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print("".join(sort_digits(a)))
