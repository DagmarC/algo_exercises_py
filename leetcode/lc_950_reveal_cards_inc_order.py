from typing import List
from collections import deque


class Solution:
    def reveal_cards_inc(self, deck: List[int]) -> List[int]:
        deck = sorted(deck, reverse=True)
        result = deque()
        
        # insert 1st element from deck (the largest one) into the queue
        result.append(deck[0])
        for n in deck[1:]:
            result.appendleft(result.pop())  # move the last element to front
            result.appendleft(n)
        return result


def main():
    # Create a binary tree
    deck = [17, 13, 11, 2, 3, 5, 7]
    deck2 = [4, 1, 2, 3]
    s = Solution()
    print(s.reveal_cards_inc(deck))
    print(s.reveal_cards_inc(deck2))


if __name__ == "__main__":
    main()
