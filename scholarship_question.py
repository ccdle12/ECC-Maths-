import pytest
import sys

# Time: O(n^2)
# Memory: O(1)
def brute_force_solution(input_TXs, target):
    current_lowest_value = 2 ** 256 - 2 ** 32 - 977
    lowest_possible_inputs = (0, 0)

    for i in range(len(input_TXs)):
        for j in range(i + 1, len(input_TXs)):
            output_values = input_TXs[i] + input_TXs[j]

            if target <= output_values < current_lowest_value:
                current_lowest_value = output_values
                lowest_possible_inputs = (input_TXs[i], input_TXs[j])

    return lowest_possible_inputs


# Time: O(n log n)
def sort_then_iterate(input_TXs, target):

    # Input transactions has only one unspent transaction
    if len(input_TXs) < 2 and input_TXs[0] >= target:
        return input_TXs[0]

    # Sort the inputs using timsort - should be O(n log n)
    input_TXs.sort()

    last_found_inputs = (0, 0)
    current_lowest_output = sys.maxsize

    low = 0
    high = len(input_TXs) - 1

    # Pointers on end and start of list, either increment or decrement points according to the lowest output compared to the target
    while low != high:
        output_values = input_TXs[low] + input_TXs[high]

        if target <= output_values < current_lowest_output:
            current_lowest_output = output_values
            last_found_inputs = (input_TXs[low], input_TXs[high])

        if output_values == target:
            break

        if output_values > target:
            high -= 1
        else:
            low += 1

    return last_found_inputs

class TestClass:
    def test_using_brute_force_solution(self):
        expected = 0.5, 0.9
        input_TXs = [2, 0.5, 5, 3, 0.9]
        target = 0.71
        result = brute_force_solution(input_TXs, target)

        assert expected == result

    def test_sort_array(self):
        expected = [0.5, 0.9, 2, 3, 5]
        input_TXs = [2, 0.5, 5, 3, 0.9]
        input_TXs.sort()
        result = input_TXs

        assert expected == result

    def test_using_sort_then_iterate_algorithm(self):
        expected = 0.5, 0.9
        input_TXs = [2, 0.5, 5, 3, 0.9]
        target = 0.71
        result = sort_then_iterate(input_TXs, target)

        assert expected == result

    def test_using_sort_then_iterate_algorithm_2(self):
        expected = 0.5, 2
        input_TXs = [2, 0.5, 5, 3, 0.9]
        target = 2.23
        result = sort_then_iterate(input_TXs, target)

        assert expected == result

    def test_using_sort_then_iterate_algorithm_3(self):
        expected = 0.5, 3
        input_TXs = [2, 0.5, 5, 3, 0.9]
        target = 3.1
        result = sort_then_iterate(input_TXs, target)

        assert expected == result

    def test_using_sort_then_iterate_algorithm_3(self):
        expected = 2, 3
        input_TXs = [2, 0.5, 5, 3, 0.9]
        target = 5
        result = sort_then_iterate(input_TXs, target)

        assert expected == result

    def test_using_sort_then_iterate_algorithm_4(self):
        expected = 0.123, 0.23
        input_TXs = [2, 0.5, 5, 3, 0.9, 10, 100, 93, 0.23, 0.005, 0.123, 0.8342, 0.00002, 0.002342, 7, 11]
        target = 0.3
        result = sort_then_iterate(input_TXs, target)

        assert expected == result

    def test_using_sort_then_iterate_algorithm_5(self):
        expected = 1, 2
        input_TXs = [2, 1]
        target = 0.71
        result = sort_then_iterate(input_TXs, target)

        assert expected == result

    def test_using_sort_then_iterate_algorithm_6(self):
        expected = 0, 0
        input_TXs = [0.2, 0.001]
        target = 0.71
        result = sort_then_iterate(input_TXs, target)

        assert expected == result

    def test_using_sort_then_iterate_algorithm_6(self):
        expected = 1
        input_TXs = [1]
        target = 0.71
        result = sort_then_iterate(input_TXs, target)

        assert expected == result

    def test_using_sort_then_iterate_algorithm_6(self):
        expected = 0, 0
        input_TXs = [0.5]
        target = 0.71
        result = sort_then_iterate(input_TXs, target)

        assert expected == result

    def test_using_sort_then_iterate_algorithm_7(self):
        expected = 0,0
        input_TXs = [0.1, 0.2, 0.3, 0.35]
        target = 0.71
        result = sort_then_iterate(input_TXs, target)

        assert expected == result

    def test_using_sort_then_iterate_algorithm_8(self):
        expected = 0,0
        input_TXs = [0.2, 0.1, 0.35, 0.3, 0.004]
        target = 0.71
        result = sort_then_iterate(input_TXs, target)

        assert expected == result

