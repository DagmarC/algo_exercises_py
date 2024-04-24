from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def arr_to_bintree(self, nums: List[int]) -> Optional[TreeNode]:

        def arr_to_tree_rec(nums, left, right):
            if left > right or left < 0 or right >= len(nums):
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = arr_to_tree_rec(nums, left, mid-1)
            root.right = arr_to_tree_rec(nums, mid+1, right)
            return root

        return arr_to_tree_rec(nums, 0, len(nums)-1)


if __name__ == "__main__":
    s = Solution()
    nums = [-10, -3, 0, 5, 9]
    root = s.arr_to_bintree(nums)
