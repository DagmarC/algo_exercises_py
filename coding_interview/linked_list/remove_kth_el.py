class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

""" 
 remove_kth_last_node: 2 pointer solutions
 -> create the temp node to point to HEAD and set both trailer and leader pointer to it (in case head to be deleted)
 -> firstly move leader and when space between trailer and leader reaches k, then move trailer
 -> when leader.next is None (the end of the linked list) then the trailer pointer 
    should correctly point tho the node right before the node to be deleted - node to be deleted is the trailer.nex
"""
def remove_kth_last_node(head: ListNode, k: int) -> ListNode: 
    first_node = ListNode()  # 1st node to make possible head removal if needed
    first_node.next = head
    
    trailer_node, leader_node = first_node, first_node 
    space = 0  # move the trailing pointer after the space between the leader and the trailer is k
    while leader_node.next:
        if space < k:
            leader_node = leader_node.next
            space += 1 
            continue
        leader_node = leader_node.next
        trailer_node = trailer_node.next
    
    # Note if space != k then there is no such node to be deleted, k is too large    
    if trailer_node.next == head and space == k:
        head = head.next
    # When the leader.next is None, you reached the end of the linked list and the trailer pointer 
    # should correctly point tho the node right before the node to be deleted - node to be deleted is the trailer.next
    trailer_node.next = trailer_node.next.next
    
    return head


def remove_kth_last_node_naive(head: ListNode, k: int) -> ListNode:

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