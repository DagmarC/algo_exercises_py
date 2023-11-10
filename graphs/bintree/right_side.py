class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def rightSideView(node, is_right, result):
    if node is None:
        return []
    
    if is_right:
        result.append(node.value)

    rightSideView(node.left, False, result)
    rightSideView(node.right, True, result)

    return result
    

if __name__ == '__main__':
    n = Node(Node(Node(None, None, 3), Node(None, None, 4), 2) , Node(None, None, 6), 1) 
    print(rightSideView(n, True, []))