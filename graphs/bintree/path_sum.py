from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        
        return Solution.hasPathSumRec(self, root, targetSum, 0, False)
        
    def hasPathSumRec(self, node: Optional[TreeNode], targetSum: int, pathSum: int, isLeaf: bool) -> bool:
        if node is None:
            return pathSum == targetSum and isLeaf
        pathSum += node.val        
        
        if node.left is None and node.right is None:
            isLeaf = True
        
        return Solution.hasPathSumRec(self, node.left, targetSum, pathSum, isLeaf) or Solution.hasPathSumRec(self, node.right, targetSum, pathSum, isLeaf)
    
    #####################
    # NICE SOLUTION
    
    # def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    #     if not root:
    #         return False
        
    #     def recur(node, cur_sum):
    #         if not node:
    #             return False
    #         if not node.right and not node.left and cur_sum + node.val == targetSum:
    #             return True
    #         return recur(node.left,cur_sum + node.val) or recur(node.right,cur_sum + node.val)
    #     return recur(root,0)
            
    

root = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)

n9 = TreeNode(9)
n10 = TreeNode(10)
n11 = TreeNode(11)
n12 = TreeNode(12)

root.left = n2
# root.right = n3

# n2.left = n4
# n2.right = n5

# n3.left = n11
# n3.right = n9

solution = Solution()
print(solution.hasPathSum(root, 1))
