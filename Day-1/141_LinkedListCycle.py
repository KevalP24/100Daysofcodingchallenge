LEETCODE SOLUTION:
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while True:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False 

FULL CODE:
from typing import Optional

class ListNode:
    def __init__(self, x: int):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while True:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False 

def main():
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next
    solution = Solution()
    print(solution.hasCycle(head))

if __name__ == "__main__":
    main()
