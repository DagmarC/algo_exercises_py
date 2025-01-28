def is_palindrome_valid(s: str) -> bool:    
    left, right = 0, len(s)-1
    valid = True
    while left <= right:
        # skip all non-alphanumeric characters from both sides
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
            
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return valid


if __name__ == "__main__":
    s = "< $ as(?) >"
    print(f"string {s} is valid? --> {is_palindrome_valid(s)}")
    
    s = "sbb s"
    print(f"string {s} is valid? --> {is_palindrome_valid(s)}")
    
    s = "<"
    print(f"string {s} is valid? --> {is_palindrome_valid(s)}")
    
    s = " = dog  ($ god >"
    print(f"string {s} is valid? --> {is_palindrome_valid(s)}")
    
    s = "L!!&KL"
    print(f"string {s} is valid? --> {is_palindrome_valid(s)}")
