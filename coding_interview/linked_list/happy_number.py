class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def happy_number(n: int) -> bool:
    """
    Happy number is defined as a number that, when repeatedly subjected to 
    the process of squaring its digits and summing those squares, eventually leads to 1.
    
    Can be understood as Problem of Linked List cycle detecion - or Floyds Cycle Detection. 
    If happy number never will be happy  - equal to 1, then there is infinite loop
    
    Example; 23 = 2ˆ2 + 3ˆ2 = 13, 1ˆ2 + 3ˆ2 = 10, 1ˆ2 + 0ˆ2 = 1 (HAPPY NUMBER)
    """
    
    slow = fast = n
    
    while True:
        # _get_squared_sum will calculate the next number that will be used in further calculations, hence it can be used as the idea of linked list next nodes
        slow = _get_squared_sum(slow)
        fast = _get_squared_sum(_get_squared_sum(fast))
        
        if fast == 1:
            return True  # Happy number has been discovered
        
        if slow == fast:
            return False  # cycle has been detected, hence n is not a happy number
        

def _get_squared_sum(n: int) -> int:
    squared_sum = 0
    while n > 0:
        digit = n % 10 # Extract the last digit
        n //= 10 # Truncate the last digit
        squared_sum += pow(digit, 2)  # Add the aquare of the digit to the extracted sum
    return squared_sum