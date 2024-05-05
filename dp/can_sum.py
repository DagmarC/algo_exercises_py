from typing import List


def canSum(target: int, arr: List[int]):
    dp = [None] * (target+1)
    dp[0] = True
    
    if dp[target] is not None:
        return dp[target]

    for n in arr:
        if target - n >= 0:
            dp[target] = canSum(target - n, arr)

    return dp[target] if dp[target] is not None else False


def main():
    print(canSum(7, [2, 4]))  # False
    print(canSum(7, [5, 3, 4, 7]))  # True
    print(canSum(1, [1]))  # True
    print(canSum(1, [2]))  # False

    



if __name__ == "__main__":
    main()
