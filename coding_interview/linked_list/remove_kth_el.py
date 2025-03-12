class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def remove_kth_last_node(head: ListNode, k: int) -> ListNode:
    # Write your code here

    def count_nodes() -> int:
        n = head
        c = 0
        while n:
            n = n.next
            c += 1
        return c
    
    count = count_nodes()
        
    curr_node = head
    prev = None
    i = 0
    
    while curr_node:
        if count-k == i and curr_node == head:
            head = curr_node.next
            
        if count-k == i and prev:
            prev.next = curr_node.next
        prev = curr_node
        curr_node = curr_node.next
        i += 1
    return head