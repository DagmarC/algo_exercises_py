class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def linked_list_intersection(head_A: ListNode, head_B: ListNode):
    n1 = head_A
    n2 = head_B
    
    # both pointers traverse m + n steps and align perfectly at the intersection or both reach None at the same time if there's no intersection.
    while n1 != n2:
        n1 = n1.next if n1 else head_B
        n2 = n2.next if n2 else head_A 
    return n1