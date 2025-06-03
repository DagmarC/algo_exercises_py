def longest_uniform_substring_after_replacements(s: str, k: int) -> int:
    max_window_size = 0
    letter_window_size = 0
    
    # Create digit frequencies with 1st starting position
    letter_freq = {} # in the form of letter: [count, 1st position]
    for i, letter in enumerate(s):
        if letter in letter_freq:
            # Update letter count - 1st in tuple
            letter_freq[letter][0] += 1
        else:
            # Add new letter to the dictionary and save it's 1st occurrence
            letter_freq[letter] = [1, i]
            
    # Sort by the first element of the tuple - the count, in descending order
    # It prevents searching for max window size with k replacements, if the following max_letter_window_size could not be greater than the current max_window_size
    sorted_letter_freq = dict(sorted(letter_freq.items(), key=lambda item: item[1][0], reverse=True))
    print(f"START: s: {s}, Letter frequencies: {sorted_letter_freq}\n")
    
    for letter, value in sorted_letter_freq.items():
        # key:letter = value, where arr represents [count, index of first occurrence] respectively
        count = value[0]
        occurrence = value[1]
        
        # We do not need to continue to find the longest uniform unique substring with k replacements, if the following condition is met:
        if max_window_size >= count+k:
            break
        
        letter_window_size = max_unique_chars_with_char_replacement(s, letter, 
                                        max(0, occurrence-k), 
                                        max(0, occurrence-k), 
                                        k)
        max_window_size = max(max_window_size, letter_window_size)
        print(f"--- String: {s},  letter: {letter}, letter max window size: {letter_window_size}, max_window_size {max_window_size}")
        
    return max_window_size

def max_unique_chars_with_char_replacement(s: str, letter: str, l: int, r: int, k: int) -> int:
    """
    With Sliding window technique try to find maximum window, where k-replacements can be done in string s with letter ch.
    When condition is violated and k <= 0, Shrink -> l++ and save current_window size if it is greater than the previous one
    When condition is met and unique char is next, Expand -> r++
    When condition is violated but k > 0, "letter  can be replaced in the string, Expand -> r++ and decrement k -> k--
    Return tuple[left, right, max window size] respectively.
    """
    print(f"Sliding window: s: {s}, letter: {letter}, l:{l}, r: {r}, k: {k}\n")
    max_window = 0
    current_window_size = 0
    while r < len(s):
        # Condition is violating and no replacements (k=0) can be done anymore
        while s[r] != letter and k <= 0:
            # If the pointer l points to the letter that is letter
            # then no replacement was done at this position so k cannot be increased when shrinking the window size,
            # otherwise l points to the letter that was virtually replaced by character letter, which means when 
            # moving with the left pointer to the right, we can increase the k by one, since the widow is moving to the right
            # letter=a, l=0, r=1, s: abc, k=0
            # --- Shrinking: letter == a, l points to letter a, so k is not increasd, l += 1
            # letter=a, l=0, r=1, s: bcaa, k=0
            # --- Shrinking: letter != a (letter == b), l points to letter b, so it was virtually replaced by letter letter=a, so k+=1 when l += 1 
            
            # Release letter replacement
            if s[l] != letter:
                k += 1  
                
            # Save the max window size
            max_window = max(max_window, current_window_size)
            
            # Shrink the window size 
            l += 1 
            current_window_size -= 1
            
        # Condition is vilating, but k > 0 --> decrement k (replace current letter at position r with character letter virtually)
        if s[r] != letter and k > 0:
            k -= 1
            
        # Expand the string - condition is now OK
        r += 1
        current_window_size += 1

    return max(max_window, current_window_size)


if __name__ == "__main__":
    longest_uniform_substring_after_replacements("bccbdabca", k=2)