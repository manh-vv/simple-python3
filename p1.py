# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

print("Hello problem 1")


def valid_multiples_of(n, d):
    return n % d == 0


def solve_p1(any_n):
    my_sum = 0
    for i in range(any_n):
        if valid_multiples_of(i, 3) or valid_multiples_of(i, 5):
            my_sum += i

    return my_sum


# solution of 10
print(f"solve problem with 10: {solve_p1(10)}")


# solution of 1000
# 233168
print(f"solve problem with 1000: {solve_p1(1000)}")
