from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  
      
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return Solution.ancestorDiffRec(self, root, root.val, root.val)
        
    def ancestorDiffRec(self, node: Optional[TreeNode], maximum: int, minimum: int) -> int:
        if node is None:
            return 0
        
        # update differrence with the current node
        current_diff = max(abs(node.val-maximum), abs(node.val-minimum))
        # update maximum and minimum if node.val is one of them
        maximum, minimum = max(node.val, maximum), min(node.val, minimum)
        
        left_diff = Solution.ancestorDiffRec(self, node.left, maximum, minimum)
        right_diff =  Solution.ancestorDiffRec(self, node.right, maximum, minimum)
        
        return max(current_diff, left_diff, right_diff)


root = TreeNode(1)
n2 = TreeNode(1)
n3 = TreeNode(8)
# n4 = TreeNode(6)
# n5 = TreeNode(1)
# n6 = TreeNode(14)
# n7 = TreeNode(7)

root.left = n2
root.right = n3

# n2.left = n6
# n2.right = n5

# n3.right = n4

# n5.right = n7


solution = Solution()
print(solution.maxAncestorDiff(root))