from typing import List

def shift_zeros_to_the_end(nums: List[int]) -> None:
    i, j = 0, 0
    while i < len(nums) and j < len(nums):
        if nums[j] == 0:
            while i < len(nums)-1 and nums[i] == 0:
                i += 1  # skip consecutive zeros
            nums[i], nums[j] = nums[j], nums[i]  # swap first occuring 0 with 1st non-zero digit
        j += 1
        i += 1   
        
        
if __name__ == "__main__":
    t1 = [1, 2, 3]
    print(f"IN: {t1}")
    shift_zeros_to_the_end(t1)
    print(f"OUT: {t1}")
    
    t1 = [0, 2, 3]
    print(f"IN: {t1}")
    shift_zeros_to_the_end(t1)
    print(f"OUT: {t1}")
    
    t1 = [0, 1, 0, 2, 3]
    print(f"IN: {t1}")
    shift_zeros_to_the_end(t1)
    print(f"OUT: {t1}")
    
    t1 = [1, 2, 3, 0]
    print(f"IN: {t1}")
    shift_zeros_to_the_end(t1)
    print(f"OUT: {t1}")
    
        
    t1 = [0, 1, 0, 2, 3, 0, 0]
    print(f"IN: {t1}")
    shift_zeros_to_the_end(t1)
    print(f"OUT: {t1}")
    
    t1 = [0, 0, 0,  2]
    print(f"IN: {t1}")
    shift_zeros_to_the_end(t1)
    print(f"OUT: {t1}")
    
    t1 = [0, 0, 0, 0, 0, 1, 2]
    print(f"IN: {t1}")
    shift_zeros_to_the_end(t1)
    print(f"OUT: {t1}")