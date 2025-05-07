class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

############## 1st solution ##############
##########################################

def palindromic_linked_list_two_lists(head: ListNode) -> bool:
    # Write your code here
    # tmpNode = ListNode(val="<Start>", next=head)  # point to the head and set ptrs to the tmp pointer
    p1, p2 = head, head
    
    # Approach: p2 is 2x faster than p1, when p2 reaches the end, p1 is in the middle 
    # -> compare the rest of p1.next - end  with the string that has been captured with p1 [start - middle]
    first_part = []
    while p2 and p2.next:
        first_part.append(p1.val)
        p1 = p1.next
        p2 = p2.next.next
        
    if p1 == p2:
        return True  # only head in the Linked List
    
    # odd number of nodes, skip the middle pointer  a->b->a->None (p1 points to b, p2 points
    if p2:
        p1 = p1.next 
        
    second_part = []
    while p1:
        second_part.append(p1.val)
        p1 = p1.next
    print(first_part, second_part, second_part[::-1])
    return first_part == second_part[::-1]

############## 2nd solution ##############
##########################################

def palindromic_linked_list_stack(head: ListNode) -> bool:
    # Write your code here
    # tmpNode = ListNode(val="<Start>", next=head)  # point to the head and set ptrs to the tmp pointer
    p1, p2 = head, head
    
    # Approach: p2 is 2x faster than p1, when p2 reaches the end, p1 is in the middle 
    # -> compare the rest of p1.next - end  with the string that has been captured with p1 [start - middle]
    first_part = []  # stack
    while p2 and p2.next:
        first_part.append(p1.val)
        p1 = p1.next
        p2 = p2.next.next
        
    if p1 == p2:
        return True  # only head in the Linked List
    
    # Odd number of nodes, skip the middle pointer  a->b->a->None (p1 points to b, p2 points to a, where a.next = None)
    if p2:
        p1 = p1.next 
        
    while p1:
        el = first_part.pop()
        if el != p1.val:
            return False
        p1 = p1.next
    
    return True

############## 3rd solution ##############
##########################################
class MatchState:
    def __init__(self):
        self.is_match = True  # boolean value is immutable, so you need a wrapper class to update the match state

def palindromic_linked_list(head: ListNode):
    # If somewhere in the recutrsion call there was not a match, it is set to False, otherwise stays True --> palindrome
    match = MatchState()
    _palindromic_linked_list_rec(head, palindromic_linked_list_len(head), match)
    return match.is_match

def _palindromic_linked_list_rec(head: ListNode, length: int, match: MatchState):
    if not head or length == 0:  # Even number of nodes
        return head
    if length == 1:  # Odd number of nodes (skipt the middle)
        return head.next
    
    result_node = _palindromic_linked_list_rec(head.next, length-2, match)
    
    # Early exit if mismatch has already been found
    if not match.is_match or not result_node:
        return result_node 
    
    # Compare current head and result_node values
    if head.val != result_node.val:
        match.is_match = False
    
    return result_node.next

def palindromic_linked_list_len(node: ListNode) -> int:
    """Returns the lenght of the linked list"""
    length = 0
    while node:
        length += 1
        node = node.next
    return length


def main():
    # Create linked list: 1 -> 2 -> 3 -> 2 -> 1
    nodes = [ListNode(1), ListNode(2), ListNode(3), ListNode(2), ListNode(1)]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    head = nodes[0]

    result = palindromic_linked_list_stack(head)
    print("Is palindrome:", result)
    
    nodes = [ListNode(1), ListNode(2), ListNode(3), ListNode(1)]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    head = nodes[0]

    result = palindromic_linked_list(head)
    print("Is palindrome:", result)

if __name__ == "__main__":
    main()