# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

cache_max_prime = 2
prime_number_set = {cache_max_prime}
prime_number_list = [cache_max_prime]


def add_new_prime(p):
    prime_number_set.add(p)
    prime_number_list.append(p)

    # update cache_max_prime
    global cache_max_prime
    cache_max_prime = p
    return


def is_known_prime(n):
    if is_dividable(n, 2):
        return False

    if n in prime_number_set:
        return True

    half_of_n = int(n / 2)

    for i in prime_number_list:
        if n % i == 0:
            return False

        if i > half_of_n:
            return True

    return False


def next_prime():
    n = cache_max_prime + 1
    while not is_known_prime(n):
        n += 1

    if n not in prime_number_set:
        add_new_prime(n)

    return n


def is_prime(n):
    if is_known_prime(n):
        return True

    half_of_n = int(n / 2)
    next_p = next_prime()
    while next_p < half_of_n:
        if n % next_p == 0:
            return False

    return True


def list_prime_less_than(n):
    while cache_max_prime < n:
        next_prime()


# test1: list all prime less than 100
# list_prime_less_than(100)
def test1():
    print(f"list number: {', '.join(map(str, prime_number_list[-9:]))}")


test1()


def is_dividable(x, y):
    return x % y == 0


def solve():
    n = 2
    aa = 600851475144

    a = aa
    half_of_a = int(a / 2)

    while half_of_a > 0 and n < half_of_a:
        while is_dividable(a, n):
            a = int(a / n)
            half_of_a = int(a / 2)

        if half_of_a == 0:
            break
        n = next_prime()

    print(f"solve: {max(a, n)}")
    test1()


# 6857
# 600851475143 / 6857 = 87625999
solve()
