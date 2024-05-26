from typing import List, Dict


def all_construct(target: str, wordBank: List[str], memo: Dict[str, List[List[str]]] = None) -> List[List[str]]:
    if memo is None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == "":
        return [[]]

    result = []
    for prefix in wordBank:
        if target.startswith(prefix):
            suffixes = all_construct(target.removeprefix(prefix), wordBank, memo)
            for suffix in suffixes:
                new_combination = suffix + [prefix]  # NEED to create a NEW list
                result.append(new_combination)

    memo[target] = result
    return result


def main():
    print(all_construct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))  # [[ab, cd, ef], [abc, def], [abcd, ef],  [ab, c, def]]
    print(all_construct("purple", ["purp", "p", "ur", "le", "purpl", "l", "e"]))  # [['purp', 'le'], ['p', ur, p, le]]
    print(all_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                        ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]))  # 0


if __name__ == '__main__':
    main()
