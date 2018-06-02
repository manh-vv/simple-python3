# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

import math

a = 9
b = 9
c = 9


def value_of_n(a, b, c):
    return a * pow(10, 5) + b * pow(10, 4) + c * pow(10, 3) + c * pow(10, 2) + b * pow(10, 1) + a * pow(10, 0)


n = value_of_n(a, b, c)
max_n = 999 * 999


def count_down_n():
    global a
    global b
    global c
    global n
    if c > 0:
        c -= 1
    elif b > 0:
        b -= 1
        if c == 0:
            c = 9
    elif a > 0:
        a -= 1
        if b == 0:
            b = 9

    n = value_of_n(a, b, c)


while n > max_n:
    count_down_n()

print(f"now n = {n}")


def solve():
    while True:
        square_of_n = int(math.sqrt(n))
        for i in range(100, 999):
            if n % i == 0:
                tmp = int(n/i)

                if tmp <= 999:
                    print(f"{n} = {i} * {tmp}")
                    return n
                elif i > square_of_n:
                    break
        count_down_n()


# 906609 = 913 * 993
# now n = 906609
solve()
print(f"now n = {n}")
