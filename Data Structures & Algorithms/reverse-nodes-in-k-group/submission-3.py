# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        gpPrev = dummy

        while True:
            kth = self.getkth(gpPrev, k)
            if not kth:
                break
            
            gpNext = kth.next
            prev, cur = gpNext, gpPrev.next
            while cur != gpNext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            tmp2 = gpPrev.next
            gpPrev.next = kth
            gpPrev = tmp2
        return dummy.next
    
    def getkth(self, cur, k):
        while cur and k > 0:
            cur = cur.next
            k -= 1
        return cur