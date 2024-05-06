from typing import List


def how_sum(target: int, arr: List[int]) -> List[int]:
    return how_sum_rec(target, arr)

    """
    The function `how_sum_rec` recursively finds a combination of elements from the input array that sum
    up to the target value.

    :param target: The `target` parameter represents the target sum that we want to achieve using
    elements from the `arr` list. The function `how_sum_rec` uses recursion to find a combination of
    elements from the `arr` list that sum up to the `target` value. If such a combination exists,
    :type target: int
    :param arr: the list of integers for the 'arr' parameter in
    the 'how_sum_rec' function. Please go ahead and provide the list of integers so that I can assist
    you further with the code
    :type arr: List[int]
    :return: The function `how_sum_rec` is returning a list of integers that sum up to the target value.
    If it is not possible to achieve the target sum using the numbers in the array, it returns `None`.
    """


def how_sum_rec(target: int, arr: List[int]) -> List[int]:
    if target == 0:
        return []

    if target < 0:
        return None

    for n in arr:
        result = how_sum_rec(target-n, arr)
        if result is not None:
            return result + [n]

    return result


def main():
    print(how_sum(7, [2, 3]))  # [3, 2, 2]
    print(how_sum(7, [5, 3, 4, 7]))  # [4, 3]
    print(how_sum(1, [1]))  # [1]
    print(how_sum(8, [2, 3, 5]))  # [2, 2, 2, 2]


if __name__ == "__main__":
    main()
