class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def palindromic_linked_list(head: ListNode) -> bool:
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

def main():
    # Create linked list: 1 -> 2 -> 3 -> 2 -> 1
    nodes = [ListNode(1), ListNode(2), ListNode(3), ListNode(2), ListNode(1)]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    head = nodes[0]

    result = palindromic_linked_list(head)
    print("Is palindrome:", result)
    
    nodes = [ListNode(1), ListNode(2), ListNode(2), ListNode(1)]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    head = nodes[0]

    result = palindromic_linked_list(head)
    print("Is palindrome:", result)

if __name__ == "__main__":
    main()