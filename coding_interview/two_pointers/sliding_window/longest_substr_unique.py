def longest_substring_with_unique_chars(s: str) -> int:
    chars = {}
    l, r = 0, 0
    max_substring = 0
    # print(f"string: {s}")
    while r < len(s):
        # print(f"--> l:{l}, r:{r} substring: {s[l:r+1]}" )
        # Add rightmost char into the dict and check if it is already present
        rightmostchar = s[r]
        
        # Add the character into the dictionary, if not present
        if rightmostchar not in chars:
            chars[rightmostchar] = 1
        else:
            chars[rightmostchar] += 1
            # Condition violation - only unique characters in the substring are allowed
            while chars[rightmostchar] > 1:
                # Decrease / delete leftmost char from the chars dict
                leftmostchar = s[l]
                # print(f".... condition violation in dict {chars}, l: {l} -> decrease leftmostchar {leftmostchar}")
                chars[leftmostchar] -= 1
                if chars[leftmostchar] == 0:
                    del(chars[leftmostchar])  # free the dictionary
                # Shrink substring
                l += 1
        # At this moment I am sure the condition is not violated, so I can update the result if the substring is longer than it was before
        max_substring = max(max_substring, r - l + 1)
        # print(f"max substring yet {max_substring}")
        r += 1
    return max_substring
   

if __name__ == "__main__":
    s = "abcbad"
    print(longest_substring_with_unique_chars(s))