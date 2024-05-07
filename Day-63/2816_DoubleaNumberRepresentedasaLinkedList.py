# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def double_util(self, head):
        if not head:
            return 0

        carry = self.double_util(head.next)
        new_val =(head.val) * 2 + carry
        head.val = new_val % 10

        return new_val // 10

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last_carry = self.double_util(head)

        if last_carry > 0:
            new_head = ListNode(last_carry)
            new_head.next = head
            return new_head

        return head
