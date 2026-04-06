# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        a, b = head, head.next

        while a and a.next and b and b.next:
            if a == b :
                return True
            a = a.next
            b = b.next.next
        return False