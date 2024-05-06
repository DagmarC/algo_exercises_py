from typing import List


def best_sum(target: int, arr: List[int]) -> List[int]:
    return best_sum_rec(target, arr)


def best_sum_rec(target: int, arr: List[int]) -> List[int]:
    if target == 0:
        return []

    result = None
    for n in arr:
        partialResult = best_sum_rec(target-n, arr) if target - n >= 0 else None
        if partialResult is not None:
            # here I already know that it is possible to create the combination
            currentResult = partialResult + [n]
            if result is None or len(result) > len(currentResult):
                result = currentResult
            
    return result


def main():
    print(best_sum(7, [2, 3, 7, 4]))  # [7]


if __name__ == "__main__":
    main()
