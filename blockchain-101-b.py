import pytest
import math
from fractions import Fraction


# From Blockchain 101 - Elliptic Curve Cryptography - https://eng.paxos.com/blockchain-101-elliptic-curve-cryptography


# How to calculate Elliptic Curves over Finite Fields
# Exercise 1
def calc_y(y, prime_num):
    return (y ** 2) % prime_num


def calc_x(x, prime_num):
    return (x ** 3 + 7) % prime_num


def is_point_in_curve(point, prime_num):
    x = point[0]
    y = point[1]

    xVal = calc_x(x, prime_num)
    yVal = calc_y(y, prime_num)

    if xVal == yVal:
        return True

    return False


def lazy_check_of_points(points, prime_num):
    # F223 is the finite field
    # y2 = x3 + 7
    results = []

    for eachPoint in points:
        x = eachPoint[0]
        y = eachPoint[1]

        results.append(is_point_in_curve((x, y), prime_num))

    return results


# /**
#  * Elliptical Curve Functions with modular arithmetic
#  *
# Algorithm:
# 1. Calculate slope_intercept
    #a. (y2 - y1)/(x2 - x1)

# 2. Take the x val of the slope intercept
    # a. slope_x = pow(x_val_slope_intercept, prime_num - 2, prime_num) : this will perform (x_val ** prime_num - 2) % prime_num

# 3. Calculate the slope that will be used in the equations to find (x3, y3)
    # a. slope = (y_val_slope_intercept * slope_x) % prime_num
    # b. Now we have the slope value between points P1 and P2, we can now use this to calculate P3

#4. Calculate x3
    # a.  x3 = (slope ** 2) - x1 - x2

#5. Calculate y3
    # a. y3 = slope * (x1 - x3) - y1

#6. Return P3
    # a. return x3, y3

def get_point3(p1, p2, prime_num):
    slope = calculate_slope_intercept(p1, p2, prime_num)
    x3 = get_x3(slope, p1, p2, prime_num)
    y3 = get_y3(slope, p1, x3, prime_num)

    return x3, y3


def calculate_slope_intercept(p1, p2, prime_num):
    # s = y2 - y1 / x2 - x1
    x1 = p1[0]
    y1 = p1[1]

    x2 = p2[0]
    y2 = p2[1]

    slope_intercept = (y2 - y1) / (x2 - x1)
    fraction = get_as_fraction(slope_intercept)

    numerator = get_numerator(fraction)
    denominator = get_denominator(fraction)

    slope_x_val = get_slope_x_val(denominator, (prime_num - 2), prime_num)
    slope = get_slope(numerator, slope_x_val, prime_num)

    return slope


def get_as_fraction(slope_intercept):
    return Fraction(slope_intercept).limit_denominator()


def get_numerator(fraction):
    return fraction.numerator ** 2


def get_denominator(fraction):
    return fraction.denominator * fraction.numerator


def get_slope_x_val(x_denominator, prime_num_minus_2, prime_num):
    return pow(x_denominator, prime_num_minus_2, prime_num)


def get_slope(numerator, slope_x_val, prime_num):
    return (numerator * slope_x_val) % prime_num


def get_x3(slope, p1, p2, prime_num):
    x1 = p1[0]
    x2 = p2[0]
    return ((slope ** 2) - x1 - x2) % prime_num


def get_y3(slope, p1, x3, prime_num):
    x1 = p1[0]
    y1 = p1[1]
    return (slope * (x1 - x3) - y1) % prime_num



class TestClass:
    # How to calculate Elliptic Curves over Finite Fields
    # Exercise 1

    def test_calc_y(self):
        expected = 81
        y = 128
        prime_num = 137
        result = calc_y(y, prime_num)

        assert expected == result

    def test_calc_x(self):
        expected = 81
        x = 73
        prime_num = 137
        result = calc_x(x, prime_num)

        assert expected == result

    def test_point_in_elliptic_curve(self):
        expected = True
        prime_num = 137
        point = (73, 128)
        result = is_point_in_curve(point, prime_num)

        assert expected == result

    def test_lazy_exercise(self):
        expected = [True, True, False, True, False]
        points = [(192, 105), (17, 56), (200, 119), (1, 193), (42, 99)]
        prime_num = 223
        result = lazy_check_of_points(points, prime_num)

        assert expected == result

    def test_can_get_fraction_denominator(self):
        expected = 175
        fraction = Fraction(0.28).limit_denominator(10000)
        result = fraction.denominator * fraction.numerator

        assert expected == result

    # Elliptical Curve Functions with modular arithmetic
    def test_get_numerator(self):
        expected = 49
        fraction = Fraction(0.28).limit_denominator()
        result = get_numerator(fraction)

        assert expected == result

    def test_get_denominator(self):
        expected = 175
        fraction = get_as_fraction(0.28)
        result = get_denominator(fraction)

        assert expected == result

    def test_get_slope_x_val(self):
        expected = 144
        result = get_slope_x_val(175, (223 - 2), 223)

        assert expected == result

    def test_get_slope(self):
        expected = 143
        numerator = 49
        slope_x_val = 144
        prime_num = 223

        result = get_slope(numerator, slope_x_val, prime_num)

        assert expected == result

    def test_calculate_slope_intercept(self):
        expected = 143
        result = calculate_slope_intercept((192, 105), (17, 56), 223)

        assert expected == result

    def test_get_x3(self):
        expected = 170
        slope = 143
        p1 = (192, 105)
        p2 = (17, 56)
        prime_num = 223
        result = get_x3(slope, p1, p2, prime_num)

        assert expected == result

    def test_get_y3(self):
        expected = 142
        slope = 143
        p1 = (192, 105)
        x3 = 170
        prime_num = 223

        result = get_y3(slope, p1, x3, prime_num)

        assert expected == result

    def test_get_point3(self):
        expected = 170, 142
        p1 = (192, 105)
        p2 = (17, 56)
        prime_num = 223
        result = get_point3(p1, p2, prime_num)

        assert expected == result


    #Exercise 1 Tests and Answers
    def test_1(self):
        expected = 170, 142
        p1 = (192, 105)
        p2 = (17, 56)
        prime_num = 223
        result = get_point3(p1, p2, prime_num)

        assert expected == result

    def test_2(self):
        expected = 60, 139
        p1 = (47, 71)
        p2 = (117, 141)
        prime_num = 223
        result = get_point3(p1, p2, prime_num)

        assert expected == result

    def test_3(self):
        expected = 47, 71
        p1 = (143, 98)
        p2 = (76, 66)
        prime_num = 223
        result = get_point3(p1, p2, prime_num)

        assert expected == result

