# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, prev = head, None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

        # # soltution 2: recursive
        # def reverse(cur, prev):
        #     if not cur:
        #         return prev
        #     else:
        #         nxt = cur.next
        #         cur.next = prev
        #         return reverse(nxt, cur)
            
        # return reverse(head, None)




#         if not head:
#             return None       
#         newhead = head
#         if head.next:
#             newhead = self.reverseList(head.next)
#             head.next.next = head
#         head.next = None

#         return newhead

        

