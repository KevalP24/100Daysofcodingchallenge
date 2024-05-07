# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None or head.next is None:
            return head

        nextNode = self.removeNodes(head.next)

        if head.val <nextNode.val:
            del head
            return nextNode

        head.next= nextNode
        return head
