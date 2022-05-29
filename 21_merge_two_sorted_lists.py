# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: 
Optional[ListNode]) -> Optional[ListNode]:
        def process_min(l1: Optional[ListNode], l2: Optional[ListNode]) -> 
(Optional[int],Optional[ListNode], Optional[ListNode]):
            if l1 is not None:
                head_l1 = l1.val
                next_l1 = l1.next
            else:
                head_l1 = None
                next_l1 = None
            if l2 is not None:
                head_l2 = l2.val
                next_l2 = l2.next
            else:
                head_l2 = None
                next_l2 = None
            if head_l1 is not None and head_l2 is not None:
                    if head_l1 <= head_l2:
                        return (head_l1, next_l1, l2)
                    else:
                        return (head_l2, l1, next_l2)
            if head_l1 is not None:
                return (head_l1, next_l1, l2)
            else:
                return (head_l2, l1, next_l2)
        
        def process_one(l1: Optional[ListNode], l2:Optional[ListNode], 
work_list: Optional[ListNode], head: Optional[ListNode]) -> 
Optional[ListNode]:
            (min, next_l1, next_l2) = process_min(l1, l2)
            if min is None:
                return head
            else:
                work_list.next = ListNode(min)
                return process_one(next_l1, next_l2, work_list.next, head)
        
        if list1 is None and list2 is None:
            return None
        else:
            (min, next_l1, next_l2) = process_min(list1, list2)
            initial_worklist = ListNode(min)
            return process_one(next_l1, next_l2, initial_worklist, 
initial_worklist)
