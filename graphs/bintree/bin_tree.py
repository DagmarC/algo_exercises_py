class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    # FI 3 2 1 --- FO 1 2 3
    if node == None:
        return [] # empty list

    result = []
    queue = [node] # root element

    while queue:
        n = queue.pop(0) # FIFO: remove 1st element from queue
        result.append(n.value)
        if n.left is not None:
            queue.append(n.left)
        if n.right is not None:
            queue.append(n.right)

    return result