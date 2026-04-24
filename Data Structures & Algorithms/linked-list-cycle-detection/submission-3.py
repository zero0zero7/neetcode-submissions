# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        one = head.next
        if head.next != None:
            two = head.next.next
        else:
            return False
        while True:
            if one == two:
                return True
            if one == None or two == None:
                return False
            one = one.next
            two = two.next
            if two == None:
                return False
            else:
                two = two.next

            
        