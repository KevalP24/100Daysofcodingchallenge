# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefix_sum = 0
        map = {}
        dummy = ListNode(0)
        dummy.next = head
        map[0] = dummy

        while head:
            prefix_sum += head.val            
            if prefix_sum in map:
                p = map[prefix_sum]
                start = p
                p_sum = prefix_sum
    
                while start != head:
                    start = start.next
                    p_sum += start.val
                    if start != head:
                        del map[p_sum]            
                p.next = start.next
            else:
                map[prefix_sum] = head
            head = head.next
        return dummy.next
