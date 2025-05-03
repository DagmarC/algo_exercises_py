class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


def linked_list_reversal_it(head: ListNode):
    if not head:
        return None
    
    node = head
    prev_node = None
    while node:
        next_node = node.next
        node.next = prev_node
        prev_node = node
        node = next_node
    
    return prev_node

def linked_list_reversal(head: ListNode):
    if (not head) or (not head.next):
        return head  # only node is returned itself
    print(f"1. head is {head.val}")
    new_head = linked_list_reversal(head.next)
    print(f"2. head is {head.val}, newhead is {new_head.val}")

    head.next.next = head
    head.next = None
    return new_head
    
    
# Helper functions for testing
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_linked_list(head):
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    return " -> ".join(values)


# Test Cases
def test_linked_list_reversal():
    # Test Case 1: Normal list
    head = create_linked_list([1, 2, 3, 4, 5])
    reversed_head = linked_list_reversal(head)
    assert print_linked_list(reversed_head) == "5 -> 4 -> 3 -> 2 -> 1"

    # Test Case 2: Single element list
    head = create_linked_list([42])
    reversed_head = linked_list_reversal(head)
    assert print_linked_list(reversed_head) == "42"

    # Test Case 3: Empty list
    head = create_linked_list([])
    reversed_head = linked_list_reversal(head)
    assert reversed_head is None

    print("All test cases passed!")


if __name__ == '__main__':
    test_linked_list_reversal()