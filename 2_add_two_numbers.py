# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def list_to_int_step(l: Optional[ListNode], work_str:str) -> int:
            if l is None:
                return work_str[::-1]
            else:
                lit = str(l.val)
                work_str += lit
                return list_to_int_step(l.next, work_str)
        
        def list_to_int(l: Optional[ListNode]) -> int:
            int_str = list_to_int_step(l, "")
            return int(int_str)
        
        def str_to_list_step(s:str, initial_node: Optional[ListNode], last_node: Optional[ListNode]) -> Optional[ListNode]:
            if s == "":
                return initial_node
            else:
                lit = s[0]
                new_node = ListNode(int(lit), None)
                last_node.next = new_node
                return str_to_list_step(s[1:], initial_node, new_node)
        
        
        int_1 = list_to_int(l1)
        int_2 = list_to_int(l2)
        result_int = int_1 + int_2
        result_str = str(result_int)[::-1]
        initial_node = ListNode(result_str[0], None)
        result = str_to_list_step(result_str[1:], initial_node, initial_node)
        return result
