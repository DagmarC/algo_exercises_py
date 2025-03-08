from typing import List, Set

# NAIVE SOLUTION: O(nlgn) -> sorting required
def longest_chain_of_consecutive_numbers_naive(nums: List[int]) -> int:
    if nums == []:
        return 0
    
    result = 1  # what is the default: 0 or 1?
    seq_count = 1
    nums.sort()  # sort numbers first
    
    for i, num in enumerate(nums):
        if i == 0:
            continue  # start at position i=1
        
        if num - nums[i-1] == 1:
            seq_count += 1
        elif num - nums[i-1] == 0:
            continue  # skip duplicate numbers in sequence and do not reset the sequence counter
        else:
            result = max(result, seq_count)
            seq_count = 1  # reset
        
    return max(seq_count, result) # if else clause did not run at all
 
 # O(n) SOLUTION with SETS:
def longest_chain_of_consecutive_numbers(nums: List[int]) -> int:
    if nums == []:
        return 0
    
    longest_seq = 0
    seq_count = 1
    nums_set: Set[int] = set(nums)
    
    for num in nums_set:
        # Start only with sequence starters
        if num - 1 not in nums_set:
            # Upward direction
            while  num + seq_count in nums_set:
                seq_count += 1
        longest_seq = max(seq_count, longest_seq)
        seq_count = 1  # reset the counter
        
    return longest_seq

if __name__ == "__main__":
    nums = [1,6,2,5,8,7,10,3]
    res = longest_chain_of_consecutive_numbers(nums)
    print(nums, res)
    
    nums_neg = [-1,-2,-3,0,1,2,3]
    res = longest_chain_of_consecutive_numbers(nums_neg)
    print(nums_neg, res)
    
    res = longest_chain_of_consecutive_numbers([])
    print([], res)
    
    nums_dup = [1,2,2,3,4,8,9,7]
    res = longest_chain_of_consecutive_numbers(nums_dup)
    print(nums_dup, res)

