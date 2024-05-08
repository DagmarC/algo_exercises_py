from typing import List


def can_construct_rec(target: str, wordBank: List[str]) -> bool:
    if target == "":
        return True

    # Important: branch to children ONLY IF PREFIX is found in the wordbank (not in the middle)
    for prefix in wordBank:
        if target.startswith(prefix):
            if can_construct_rec(target.removeprefix(prefix), wordBank):
                return True
    return False


def can_construct_dp(target: str, wordBank: List[str], dp=None) -> bool:
    if dp is None:
        dp = {"": True}

    if target in dp:
        return dp[target]

    if target == "":
        return True

    # Important: branch to children ONLY IF PREFIX is found in the wordbank (not in the middle)
    for prefix in wordBank:
        if target.startswith(prefix):
            if can_construct_dp(target.removeprefix(prefix), wordBank, dp):
                dp[target] = True
                return True
    dp[target] = False
    return False
