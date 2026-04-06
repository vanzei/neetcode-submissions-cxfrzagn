# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        
        gP = dummy

        while True:
            kth = self.grepK(gP, k)
            if not kth:
                break
            gN = kth.next

            prev, cur = gN, gP.next

            while cur != gN:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            tmp2 = gP.next
            gP.next = kth
            gP = tmp2
        
        return dummy.next

            
    
    def grepK(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -=1
        return curr
        
                