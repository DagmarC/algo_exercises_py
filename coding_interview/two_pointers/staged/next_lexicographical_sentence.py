def next_lexicographical_sequence(s: str) -> str:
    if len(s) <= 1:
        return s
    
    ls = list(s)  # better for manipulation
    i = len(ls) - 2
    
    # Step 1: Find the first decreasing character from the right
    while i >= 0 and ls[i] >= ls[i+1]:
        i -= 1
    
    # If no such character is found, return the reversed string (last permutation)
    if i == -1:
        return ''.join(ls[::-1]) # reverse string
    
    # Step 2: Find the smallest character on the right that is larger than ls[i]
    j = len(ls) - 1
    
    # Right part is cosidered to be Non-decreasing (the first increasing sequence was already found with i index), 
    # so the 1st element found from the right that is greater than s[i] is surely the first smallest element greater than s[i]
    while ls[j] <= ls[i]:
        j -= 1 # skip smaller elements
    
    # Step 3: Swap elements s[i] and s[j]
    ls[i], ls[j] = ls[j], ls[i]
    
    # Step 4: Sort right part from s[i+1]  - Reverse it (already non-decreasing)
    ls[i+1:] = reversed(ls[i+1:])
    
    return ''.join(ls)

# NOTES: print statements for debug:

# def next_lexicographical_sequence(s: str) -> str:
#     if len(s) == 1:
#         return s
#     print(f"start string: {s}")
    
#     i = len(s) - 2
#     while i >= 0 and s[i] >= s[i+1]:
#         i -= 1
#     print(f"i: {i} s[i] {s[i]}")
#     if i == -1:
#         return s[::-1] # reverse string
    
#     suffix = ""
#     j = i+1
#     while j <= len(s) - 1:
#         inserted = False
#         if suffix == "":
#             suffix += s[j]
#         # do the insertion sort into the suffix to have them alphabetically sorted when inserting
#         else:
#             for si, char in enumerate(suffix):
#                 if char > s[j]:
#                     suffix = suffix[:si] + s[j] + suffix[si:]
#                     inserted = True
#                     break # insertion of s[j] successfull
#             if not inserted:
#                 suffix += s[j]  # insert at the end
                
#         print(f"suffix {suffix}, sj {s[j]}")
#         j += 1
#     # Suffix is sorted, so we can swap s[i] and s[i+1]
#     result = s[:i]
#     print(f"prefix {s[:i+1]}")
    
#     #  swap s[i] and first greater letter in suffix than s[i]
#     for si, char in enumerate(suffix):
#         if s[i] < char:
#             result += char
#             print(f"swap att {result} with char {char}")
#             suffix = suffix[:si] + s[i] + suffix[si+1:]
#             print(f"swap suffix {suffix} with [s[i]] {s[i]}")
#             break     
#     result += suffix
#     return result

if __name__ == "__main__":
    s = "abcd"
    print(next_lexicographical_sequence(s))
    
    s = "dcba"
    print(next_lexicographical_sequence(s))
    
    s = "abcedda"
    print(next_lexicographical_sequence(s))  # abdacde
    
    s = "ab"
    print(next_lexicographical_sequence(s))
    
    s = "babb"
    print(next_lexicographical_sequence(s))
    