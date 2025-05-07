class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def linked_list_loop(head: ListNode) -> bool:
    slow, fast = head, head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:  # if cycle exists, they will be the same at some point, check must be after ptrs are moved since they both start at head
            return True
    return False