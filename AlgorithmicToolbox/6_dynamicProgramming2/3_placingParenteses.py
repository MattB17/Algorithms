#python3
import sys
import re


def compute_exp(a, b, operand):
    if operand == "+":
        return a + b
    if operand == "-":
        return a - b
    if operand == "*":
        return a * b
    assert False



def optimize_expression(digits, operands):
    """Note: exps stores both the max and min expressions
    to save space. Max expression's are stored in the array at
    position [i, j] with i < j and min expressions are stored
    at position [i, j] with j < i. When i = j, the min and max
    are the same as it is just a single digit.

    """
    n = len(digits)
    exps = [[None for _ in range(n)]
            for _ in range(n)]
    for i in range(n):
        exps[i][i] = digits[i]
    for diff in range(1, n):
        for i in range(0, n-diff):
            j = i + diff
            min_exp = None
            max_exp = None
            for k in range(i, j):
                a = compute_exp(exps[i][k], exps[k+1][j], operands[k])
                b = compute_exp(exps[i][k], exps[j][k+1], operands[k])
                c = compute_exp(exps[k][i], exps[k+1][j], operands[k])
                d = compute_exp(exps[k][i], exps[j][k+1], operands[k])
                min_exp = min(a, b, c, d) if min_exp is None else min(min_exp, a, b, c, d)
                max_exp = max(a, b, c, d) if max_exp is None else max(max_exp, a, b, c, d)
            exps[i][j] = max_exp
            exps[j][i] = min_exp
    return exps[0][n-1]



if __name__ == "__main__":
    expression = input().strip()
    digits = [int(x) for x in re.split("\+|-|\*", expression)]
    operands = [x for x in re.split("[0-9]", expression) if x != ""]
    print(optimize_expression(digits, operands))
