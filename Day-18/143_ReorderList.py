class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return
        stack = []
        curr = head

        while curr:
            stack.append(curr)
            curr = curr.next
        
        k = len(stack) // 2
        curr = head

        while k > 0:
            topNode = stack.pop()
            temp = curr.next
            curr.next = topNode
            topNode.next = temp
            curr = temp
            k -= 1
        curr.next = None
