# to manage letter counts more efficiently
from collections import Counter

def substring_anagrams(s: str, t: str) -> int:
    
    def _create_word_dict(word: str) -> dict[str, int]:
        word_dict = {}
        # Create dict of letter:count for word t
        for letter in word:
            if letter in word_dict:
                word_dict[letter] += 1
            else:
                word_dict[letter] = 1
        return word_dict

    def _check_anagram(anagram: str, letters: dict[str, int]) -> bool:
        """
        Check if the word 'anagram' is anagram (word formed by rearraging the letters 
        of another word using all the original letters exaclty once).
        """
        print(f"Check anagram {anagram} for {letters}")
        anagram_dict = _create_word_dict(anagram)
        return all(count == letters[letter] if letter in letters else False for letter, count in anagram_dict.items())
    
    fixed_window_size = len(t)
    n = len(s)
    l, r = 0, 0

    t_dict = _create_word_dict(t)
    result = 0
    while r < n:
        # Only exapnd the right pointer until window size is met, when window size is met, you can process each iteration
        if r - l + 1 >= fixed_window_size:
            result += 1 if _check_anagram(s[l:r+1], t_dict) else 0
            l += 1
        r += 1
        
    return result

############### COUNTER EFFICIENT WAY ###############
#####################################################

def substring_anagrams(s: str, t: str) -> int:
    """
    Counter is a subclass of dict that is used to count hashable objects.
    It is an unordered collection where elements are stored as dictionary keys
    and their counts are stored as dictionary values.

    Each count is initialized to zero and incremented for each occurrence
    of the element.

    Common use cases:
    - Counting characters in a string
    - Counting words in a list
    - Comparing frequency of elements
    - Performing multiset operations like addition, subtraction, intersection, and union

    Examples:
    ---------
    >>> from collections import Counter

    # Count characters in a string
    >>> Counter("banana")
    Counter({'a': 3, 'n': 2, 'b': 1})

    # Count elements in a list
    >>> Counter([1, 2, 2, 3, 3, 3])
    Counter({3: 3, 2: 2, 1: 1})

    # Update counts
    >>> c = Counter("hello")
    >>> c.update("world")
    >>> c
    Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, 'w': 1, 'r': 1, 'd': 1})

    # Subtract counts
    >>> c.subtract("low")
    >>> c
    Counter({'l': 2, 'o': 1, 'h': 1, 'e': 1, 'r': 1, 'd': 1, 'w': 0})  # zero-count keys remain

    # Comparison
    >>> Counter("abc") == Counter("bca")
    True

    # Arithmetic
    >>> Counter("aabbcc") + Counter("ab")
    Counter({'a': 3, 'b': 3, 'c': 2})

    >>> Counter("aabbcc") - Counter("abc")
    Counter({'a': 1, 'b': 1, 'c': 1})

    >>> Counter("aabbcc") & Counter("abc")  # intersection: min counts
    Counter({'a': 1, 'b': 1, 'c': 1})

    >>> Counter("aabbcc") | Counter("abc")  # union: max counts
    Counter({'a': 2, 'b': 2, 'c': 2})
"""
    if len(t) > len(s):
        return 0
    
    t_count = Counter(t)
    window_count = Counter(s[:len(t)])
    result = 0
    
    for i in range(len(t), len(s)):
        new_letter = s[i]
        start_letter = s[i-len(t)]
        
        # Remove leftmost character from window
        window_count[start_letter] -= 1
        if window_count[start_letter] == 0:
            del window_count[start_letter]  # free memmory

        # Add new rightmost letter to window
        window_count[new_letter] += 1
        
        if window_count == t_count:
            result += 1
            
    return result

# Main function call
if __name__ == "__main__":
    s = "caabab"
    t = "aba"
    print(substring_anagrams(s, t))  # Output: number of anagram substrings