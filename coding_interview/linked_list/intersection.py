class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def linked_list_intersection(head_A: ListNode, head_B: ListNode):
    n1 = head_A
    n2 = head_B
    
    inter_node = None
    while n1 and n2:
        if n1 == n2:
            break
            
        if n1.next == n2:
            n1 = n1.next
        elif n2.next == n1:
            n2 = n2.next
        else:
            n1 = n1.next
            n2 = n2.next  
    
    # At the point of intersection, at the end both must be None
    while n1 and n2 and n1 == n2:
        if not inter_node:
            inter_node = n1
        n1 = n1.next
        n2 = n2.next
            
    return inter_node if (not n1) and (not n2) else None