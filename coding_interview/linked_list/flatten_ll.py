from collections import deque

class MultiLevelListNode:
    def __init__(self, val=None, next=None, child=None):
        self.val = val
        self.next = next
        self.child = child

def flatten_multi_level_list(head: MultiLevelListNode) -> MultiLevelListNode:
    """"
    Flatten the multi-level linked list into a single-level linked list by linking the end of each level to the start of the next one.
    
    Input: It is a nested list representation of a multi-level linked list. 
        Each element in the list represents a node which includes a value and a child list, 
        with the entire data structure using the following structure: [[val_1, [child_list_1]], [val_2, [child_list_2]], ...]
    """
    
    flatten_list_node: MultiLevelListNode = None
    flatten_list_head: MultiLevelListNode = None
    
    queue: MultiLevelListNode = deque()  # holds  linked lists order level by level, starting with Level 1
    
    queue.append(head)
    while queue:
        current_node = queue.popleft()  # get first list inserted (FIFO)
        while current_node:
            new_node = MultiLevelListNode(val=current_node.val)
            # create the head of the flatten
            if not flatten_list_head:
                flatten_list_head = new_node
                flatten_list_node = new_node
            else:
                flatten_list_node.next = new_node
                flatten_list_node = flatten_list_node.next
                
            if current_node.child:
                queue.append(current_node.child)
            current_node = current_node.next
            
    return flatten_list_head