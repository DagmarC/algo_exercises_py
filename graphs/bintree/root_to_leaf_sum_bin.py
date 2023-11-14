from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def sumRootToLeafRec(self, node: Optional[TreeNode], binString: str) -> int:
            if node is None:
                return 0
            if node.val > 1 or node.val < 0:
                raise TypeError("ERROR VALUE: Only 0s and 1s are allowed.")
        
            binString += str(node.val) 
        
            if node.left is None and node.right is None:
                return int(binString, 2)
            
            return sumRootToLeafRec(self, node.left, binString) + sumRootToLeafRec(self, node.right, binString)
         
        return sumRootToLeafRec(self, root, "")
 
 
root = TreeNode(1)
n2 = TreeNode(0)
n3 = TreeNode(1)
n4 = TreeNode(1)
n5 = TreeNode(1)
n6 = TreeNode(0)
n7 = TreeNode(1)

root.left = n2
root.right = n3

n2.left = n4

n3.left = n5
n3.right = n6

n5.right = n7

solution = Solution()
print(solution.sumRootToLeaf(root))     

# You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents 
# a binary number starting with the most significant bit.
# For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
# For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

# Example 1:

# Input: root = [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
# Example 2:

# Input: root = [0]
# Output: 0
