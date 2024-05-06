from typing import List, Optional


def how_sum(target: int, arr: List[int]) -> List[int]:
    return how_sum_rec(target, arr)


def how_sum_rec(target: int, arr: List[int], dp: Optional[List[int]] = None) -> List[int]:
    if dp is None:
        dp = {0: []}
        
    if target in dp:
        return dp[target]

    if target == 0:
        return []

    if target < 0:
        return None

    for n in arr:
        result = how_sum_rec(target-n, arr, dp)
        if result is not None:
            dp[target] = result + [n]
            return dp[target]

    dp[target] = None
    return dp[target]


def main():
    print(how_sum(7, [2, 3]))  # [3, 2, 2]
    print(how_sum(7, [5, 3, 4, 7]))  # [4, 3]
    print(how_sum(1, [1]))  # [1]
    print(how_sum(8, [2, 3, 5]))  # [2, 2, 2, 2]
    print(how_sum(300, [13, 1, 10]))
    print(how_sum(17, [13, 12]))  # None


if __name__ == "__main__":
    main()
