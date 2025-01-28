from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def rightSideView(root):
    if root is None:
        return []
        
    result = []
    queue = deque() 
    height = 0
    
    queue.append((root, height))    
    while queue:        
        n, height = queue.popleft()  # FIFO: remove 1st element from queue
        
        if len(queue) == 0 or height < queue[0][1]:  # no more elements on the same level (with the same hight) has left -> rightmost element
            result.append(n.val)
        
        if n.left is not None:
            queue.append((n.left, height+1))
        if n.right is not None:
            queue.append((n.right, height+1))

    return result
    

if __name__ == '__main__':
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
    root.right = n3
    n2.left = n4
    n2.right = n5
    n4.left = n6
    n4.right = n7
    n7.left = n8
    n7.right = n9

    print(rightSideView(root))