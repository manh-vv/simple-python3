# Each new term in the Fibonacci sequence is generated by adding the previous two terms.
# By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.


def is_even(n):
    return n % 2 == 0


def next_fibonacci(f1, f2):
    return f1 + f2


max_value = 4_000_000


def solve_p2():
    my_sum = 0
    f1 = 0
    f2 = 1

    fn = next_fibonacci(f1, f2)
    while fn <= max_value:
        if is_even(fn):
            my_sum += fn

        # next number
        f1 = f2
        f2 = fn
        fn = next_fibonacci(f1, f2)

    return my_sum


# solve problem 2: 4613732
print(f"sum of the even-valued terms: {solve_p2()}")
