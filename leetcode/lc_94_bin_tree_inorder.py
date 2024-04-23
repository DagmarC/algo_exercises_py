from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder_traversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder_traversal_rec(node: Optional[TreeNode]) -> List[int]:
            if node is None:
                return []
            inorder_traversal_rec(node.left)
            result.append(node.val)
            inorder_traversal_rec(node.right)
            return result

        return inorder_traversal_rec(root)
    
    def inorder_traversal2(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        return (
            self.inorder_traversal2(root.left) +
            [root.val] +
            self.inorder_traversal2(root.right)
        )

