from typing import List


def best_sum(target: int, arr: List[int]) -> List[int]:
    return best_sum_rec(target, arr)


def best_sum_rec(target: int, arr: List[int], dp=None) -> List[int]:
    if dp is None:
        dp = {0: []}

    if target in dp:
        return dp[target]

    if target == 0:
        return []

    result = None
    for n in arr:
        partialResult = best_sum_rec(target-n, arr, dp) if target - n >= 0 else None
        if partialResult is not None:
            # here I already know that it is possible to create the combination
            currentResult = partialResult + [n]
            if result is None or len(currentResult) < len(result):
                result = currentResult

    dp[target] = result  # result stores the shortest combination for the target sum
    return result


def main():
    print(best_sum(7, [2, 3, 7, 4]))  # [7]
    print(best_sum(8, [2, 3, 5]))  # [3, 5]
    print(best_sum(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]


if __name__ == "__main__":
    main()
