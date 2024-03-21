LEETCODE SOLUTION:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cuurent = head
        while cuurent is not None:
            temp = cuurent.next
            cuurent.next = prev
            prev = cuurent
            cuurent = temp
        head = prev
        return head
        
