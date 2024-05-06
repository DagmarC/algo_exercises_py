from typing import List, Optional


def can_sum(target: int, arr: List[int]) -> bool:
    dp = [None] * (target+1)
    dp[0] = True
    return can_sum_rec(target, arr, dp)


def can_sum_rec(target: int, arr: List[int], dp: Optional[List[bool]] = None) -> bool:
    if dp[target] is not None:
        return dp[target]

    if target == 0:
        return True

    for n in arr:
        if target - n >= 0:
            dp[target] = can_sum_rec(target - n, arr, dp)

    return dp[target] if dp[target] is not None else False


def main():
    print(can_sum(7, [2, 4]))  # False
    print(can_sum(7, [5, 3, 4, 7]))  # True
    print(can_sum(1, [1]))  # True
    print(can_sum(100, [2, 1, 3, 4, 50]))  # True
    print(can_sum(300, [7, 14]))  # False


if __name__ == "__main__":
    main()
