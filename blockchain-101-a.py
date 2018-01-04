import pytest
import math


# From Blockchain 101 - Foundational Math - https://eng.paxos.com/blockchain-101-foundational-math

# Finite Fields:
# A set of integers in a field
# If we add, subtract, multiply or divide -
# anything other than 0 and then % by the finite field length, -
# The result will always be an integer within the finite field

# Finite Fields Example:

# F19 = {0,1,2...18}

# Finite Field Functions
def finite_field_addition(x, y, finite_field):
    return (x + y) % finite_field


def finite_field_multiplication(x, y, finite_field):
    return (x * y) % finite_field


def series_finite_field(finite_field, constant_k):
    field_range = range(1, finite_field - 1)
    result = 0

    for number in field_range:
        result = (number * constant_k) % finite_field
        print("series output: {0}".format(result))

    return result


def series_pow_finite_field(finite_field, constant_k):
    field_range = range(1, finite_field - 1)
    result = 0

    for number in field_range:
        result = (number ** constant_k) % finite_field
        print("series output: {0}".format(result))

    return result


def finite_field_division(x, y, p):
    return (x * (y ** (p - 2))) % p


def fermats_little_theorem(n, p):
    # a^p-1 = 1 (mod p)

    if is_number_prime(p) == False:
        return "P is not prime"

    return math.pow(n, p - 1) % p


def is_number_prime(p):
    # Time Complexity: O(sqrt(n)-2)

    sqr_root_p = math.ceil(math.sqrt(p))

    for i in range(2, sqr_root_p):
        modulo_result = p % i
        if (modulo_result == 0):
            print("value of p: {0}".format(p))
            print("Divisible number found: {0}".format(i))
            return False

    return True


# Exercise for Finite Fields MULTIPLICATION from url: https://eng.paxos.com/blockchain-101-foundational-math
# 3.
series_finite_field(31, 3)  # All the results are shown as print, and all the results are members of the finite field

# 4.
print("Starting power finite field")
series_pow_finite_field(31, 30)  # All the results will be 1


# /**
#  * Elliptical Curve Functions
#  *
def calculate_slope_intercept(x1, y1, x2, y2):
    # s = y2 - y1 / x2 - x1
    return (y2 - y1) / (x2 - x1)


def calculate_x3(slope, x1, x2):
    # S^2 -x1 -x2
    return (slope ** 2) - x1 - x2


def calculate_y3(slope, x1, x3, y1):
    # y3 = S(x1 - x3) - y1
    return (slope * (x1 - x3)) - y1


def calculate_p3(p1, p2):
    x1 = p1[0]
    y1 = p1[1]

    x2 = p2[0]
    y2 = p2[1]

    slope = calculate_slope_intercept(x1, y1, x2, y2)
    x3 = calculate_x3(slope, x1, x2)
    y3 = calculate_y3(slope, x1, x3, y1)

    return x3, y3


def verify_point_in_elliptic_curve(x3, y3):
    y = y3 ** 2
    x = (x3 ** 3) + (5 * x3) + 7

    if y == x:
        return True

    return False


class TestClass:

    # Addition function tests for finite fields
    def test_add_a(self):
        result = finite_field_addition(11, 6, 19)
        expected = 17
        assert result == expected

    def test_add_b(self):
        result = finite_field_addition(17, 6, 19)
        expected = 4
        assert result == expected

    def test_add_c(self):
        result = finite_field_addition(8, 14, 19)
        expected = 3
        assert result == expected

    def test_add_d(self):
        result = finite_field_addition(4, -12, 19)
        expected = 11
        assert result == expected

    # Multiplication function tests for finite fields
    def test_multiply_a(self):
        result = finite_field_multiplication(24, 19, 31)
        expected = 22
        assert result == expected
        assert result <= 31

    def test_pow_a(self):
        result = 17 ** 3 % 31
        expected = 15
        assert result == expected
        assert result <= 31

    # 1*k...30*k function tests for finite fields
    def test_series_a(self):
        result = series_finite_field(31, 5)
        expected = 21
        assert result == expected

    def test_series_b(self):
        result = series_finite_field(31, 30)
        expected = 2
        assert result == expected

    def test_pow_series_a(self):
        result = series_pow_finite_field(31, 30)
        expected = 1
        assert result == expected

    # Division function test for finite fields
    def test_finite_field_division(self):
        result = finite_field_division(2, 3, 19)
        expected = 7
        assert result == expected

    def test_finite_field_division_2(self):
        result = finite_field_division(3, 15, 19)
        expected = 4
        assert result == expected

    # Testing Fermats Little Theorem
    def test_fermats_little_theorem(self):
        # Tests that result of a^prime_num - a
        # the prime_num is a multiple
        n = 2
        prime_num = 19
        a_pow_to_p = ((n ** prime_num) - 1) % prime_num

        assert a_pow_to_p == 1

    def test_fermats_little_theorem(self):
        n = 5
        prime_num = 11
        expected = 1
        result = fermats_little_theorem(n, prime_num)
        assert expected == result

    def test_fermats_little_theorem_2(self):
        n = 2
        prime_num = 8
        expected = "P is not prime"
        result = fermats_little_theorem(n, prime_num)
        assert expected == result

    def test_fermats_little_theorem_3(self):
        n = 2
        prime_num = 8
        expected = "P is not prime"
        result = fermats_little_theorem(n, prime_num)
        assert expected == result

    # Testing helper function for if number is prime
    def test_is_number_prime(self):
        expected = True
        result = is_number_prime(19)

        assert result == expected

    def test_is_number_prime_2(self):
        expected = False
        result = is_number_prime(6)

        assert result == expected

    def test_is_number_prime_3(self):
        expected = True
        result = is_number_prime(7)

        assert result == expected

    def test_is_number_prime_5(self):
        expected = False
        result = is_number_prime(150)

        assert result == expected

    # Exercise for Finite Fields MULTIPLICATION from url: https://eng.paxos.com/blockchain-101-foundational-math
    def test_exercise_multiplication_finite_field_1(self):
        expected = 22
        result = finite_field_multiplication(24, 19, 31)
        assert result == expected

    def test_exercise_multiplication_finite_field_2(self):
        expected = 15
        result = finite_field_multiplication(17, (17 ** 2), 31)
        assert result == expected

    def test_exercise_multiplication_finite_field_3(self):
        expected = 16
        result = finite_field_multiplication((5 ** 5), 18, 31)
        assert result == expected

    # Exercise for Finite Fields from url: https://eng.paxos.com/blockchain-101-foundational-math
    # 1.
    def test_finite_field_division_1(self):
        expected = 4
        result = finite_field_division(3, 24, 31)
        assert expected == result

    def test_calculate_slope_intercept(self):
        expected = 2
        result = calculate_slope_intercept(2, 5, 3, 7)

        assert expected == result

    def test_calculate_x3(self):
        expected = -1
        slope = calculate_slope_intercept(2, 5, 3, 7)
        result = calculate_x3(slope, 2, 3)

        assert result == expected

    def test_calculate_y3(self):
        expected = 1
        slope = calculate_slope_intercept(2, 5, 3, 7)
        x3 = calculate_x3(slope, 2, 3)
        result = calculate_y3(slope, 2, x3, 5)

        assert expected == result

    def test_unpacking_tuples(self):
        expected = 2
        p1 = (2, 5)
        result = p1[0]

        assert expected == result

    def test_calculate_p3(self):
        expected = (-1, 1)
        p1 = (2, 5)
        p2 = (3, 7)
        result = calculate_p3(p1, p2)

        assert expected == result

    def test_verify_point_in_elliptic_curve(self):
        expected = True
        x3 = calculate_x3(2, 2, 3)
        y3 = calculate_y3(2, 2, x3, 5)

        result = verify_point_in_elliptic_curve(x3, y3)
        assert expected == result
