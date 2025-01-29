from typing import List

def largest_container(heights: List[int]) -> int:
    left, right = 0, len(heights) - 1
    max_volume = 0
    
    while left < right:
        # anonymous function that will calculate the current height of the container and updates left and right indices, return: volume, left, right
        max_container = lambda l, r: (heights[left] * (right - left), left + 1, right) if heights[left] <= heights[right] else (heights[right] * (right - left), left, right - 1)
        volume, left, right = max_container(left, right)
        max_volume = volume if volume > max_volume else max_volume
    
    return max_volume

# Notes: 
# max_volume is determined by height * width of the rectangle given by formula: min(heights[left], heights[right]) * (right - left)
# Without lambda impl. there are 3 cases to move pointers inward: 
#   height [left] < height[right] -> left++
#   height [left] > height[right] -> right--
#   height [left] = height[right] -> left++, right--