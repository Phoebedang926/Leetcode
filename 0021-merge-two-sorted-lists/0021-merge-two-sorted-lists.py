# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2

        return dummy.next

    






        # p1, p2 = list1, list2
        # while p1 or p2:
        #     if not p1:
        #         return None      
        #     if not p2:
        #         return None                      
        #     nxt1 = p1.next
        #     nxt2 = p2.next
        #     if p1.val <= p2.val:
        #         p1.next = p2
        #     else: 
        #         p2.next = p1
        #     p1 = nxt1
        #     p2 = nxt2
        # return p1

