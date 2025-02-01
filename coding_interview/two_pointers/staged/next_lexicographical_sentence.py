def next_lexicographical_sequence(s: str) -> str:
    if len(s) == 1:
        return s
    
    i = len(s) - 2
    # find 1st occurence where the letter is greater than its rightmost neighbour
    while i >= 0 and s[i] >= s[i+1]:
        i -= 1
    
    # if there is no increasing two consecutive letters found like dcba, return just its reverse abcd
    if i == -1:
        return s[::-1] # reverse string
    
    suffix = ""
    j = i+1
    # go through the string s from j=i+1 to the end and sort this suffix alphabetically 
    while j <= len(s) - 1:
        inserted = False
        if suffix == "":
            suffix += s[j]
        # do the 'insertion sort' into the suffix to have them alphabetically sorted, which will be used in the result
        else:
            for si, char in enumerate(suffix):
                if char > s[j]:
                    suffix = suffix[:si] + s[j] + suffix[si:]
                    inserted = True
                    break # insertion of s[j] successfull
            if not inserted:
                suffix += s[j]  # no char in suffix was greater than s[j] so s[j] is the largest => insert at the end                
        j += 1
        
    # Suffix is sorted, so we can now form the result and swap s[i] and s[j] where s[j] is the first smallest letter greater than s[i]
    result = s[:i]
    
    #  swap s[i] and first greater letter in suffix than s[i]
    for sj, char in enumerate(suffix):
        if s[i] < char:
            result += char # char represents s[j]
            suffix = suffix[:sj] + s[i] + suffix[sj+1:]  # swap s[i] and s[j]
            break     
    result += suffix  # add swapped suffix to the result
    
    return result

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
    