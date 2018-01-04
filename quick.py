import math


def fast_is_number_prime(n):
    steps = 0

    # Catch all the small prime numbers first
    if n % 2 == 0:
        return False, steps

    if n % 3 == 0:
        return False, steps

    if n % 5 == 0:
        return False, steps

    if n % 7 == 0:
        return False, steps

    # Get the square root and use it as the upper bound for iteration
    upper_bound = int(math.sqrt(n))
    print("Upper bound {0}".format(upper_bound))

    # Start iterating from the next small prime number : 11
    i = 11
    while i < upper_bound:
        steps += 1

        # Check if performing modulo on using i has 0 remainder,
        if n % i == 0 or n % (i + 2) == 0:
            return False

        # By iterating +6 we are iterating most of the time on a prime number by starting from 11
        i += 6

    return True, steps


def slow_is_number_prime(n):
    upper_bound = int(math.sqrt(n))
    print("Upper bound {0}".format(upper_bound))

    i = 3
    steps = 0

    if n % 2 == 0:
        return False, steps

    while i < upper_bound:
        steps += 1
        print("SLOW: Steps: {0}".format(i))

        if n % i == 0:
            return False, steps

        i += 2

    return True, steps


fast = fast_is_number_prime(54673257461630679457)
slow = slow_is_number_prime(54673257461630679457)

print("Fast: {0}".format(fast))
print("Slow: {0}".format(slow))
