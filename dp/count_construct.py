from typing import List

# PLEASE DO NOT FORGET TO PASS MEMO OBJECT DP IN RECURSIVE CALL


def count_construct(target: str, wordBank: List[str], dp=None):
    if dp is None:
        dp = {"": 1}

    if target in dp:
        return dp[target]

    if target == "":
        return 1

    result = 0
    for prefix in wordBank:
        if target.startswith(prefix):
            result += count_construct(target.removeprefix(prefix), wordBank, dp)
       
    dp[target] = result
    return result


def main():
    print(count_construct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # 1
    print(count_construct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))  # 4
    print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                          ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # 0
    print(count_construct("purple", ["purp", "p", "ur", "le", "purpl"]))  # 2


if __name__ == '__main__':
    main()
