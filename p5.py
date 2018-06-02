# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import math

current_max_prime_number = 3
prime_numbers = [2, current_max_prime_number]


def next_prime_number():
    global current_max_prime_number

    while True:
        current_max_prime_number += 2
        prime_flag = True
        half_of_n = int(current_max_prime_number / 2)

        for p in prime_numbers:
            if current_max_prime_number % p == 0:
                prime_flag = False
                break

            if p > half_of_n:
                break

        if prime_flag:
            prime_numbers.append(current_max_prime_number)
            return current_max_prime_number


def factoring_number(n):
    rs = {}
    for p in prime_numbers:
        if n % p == 0:
            count_p = 0
            while n % p == 0:
                count_p += 1
                n = n / p
            rs[p] = count_p

    while n > current_max_prime_number:
        p = next_prime_number()
        if n % p == 0:
            count_p = 0
            while n % p == 0:
                count_p += 1
                n = n / p
            rs[p] = count_p

    return rs


def solve(n):
    rs = {}
    for i in range(2, n):
        fs = factoring_number(i)
        for k, v in fs.items():
            if k in rs:
                if rs[k] < v:
                    rs[k] = v
            else:
                rs[k] = v

    m = 1
    for k, v in rs.items():
        m *= math.pow(k, v)

    print(rs)

    return int(m)


k = 10
print(f"solve({k}) = {solve(k)}")

# 232792560
k = 100
print(f"solve({k}) = {solve(k)}")
