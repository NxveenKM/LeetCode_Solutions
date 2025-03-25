# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)  # Dummy node to simplify result list creation
        current = dummy_head  # Pointer to build the new list
        carry = 0  # Initialize carry to 0
        
        # Loop until both lists are processed
        while l1 is not None or l2 is not None:
            # Get the values from the current nodes, or 0 if the node is None
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            # Calculate the sum and the new carry
            total = val1 + val2 + carry
            carry = total // 10  # Update carry for the next iteration
            current.next = ListNode(total % 10)  # Create a new node with the digit
            
            # Move to the next nodes in the lists
            current = current.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        # If there's a carry left, add a new node
        if carry > 0:
            current.next = ListNode(carry)
        
        # Return the next node of dummy_head, which is the head of the result list
        return dummy_head.next
