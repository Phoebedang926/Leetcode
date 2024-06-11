# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        def mergeList(list1, list2):
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
            elif list2:
                tail.next = list2            
            return dummy.next
        
        while len(lists) > 1:
            mergeLists = []
        
            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i+1] if (i + 1) < len(lists) else None
                mergeLists.append(mergeList(list1, list2))
            lists = mergeLists
            
        return lists[0]
            
        
    

                
            
            
        