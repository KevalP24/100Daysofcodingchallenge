LEETCODE SOLUTION:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if (slow==fast):
                slow = head
                while slow!=fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

FULL CODE:
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None

def main():
    # Example usage
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next  

    solution = Solution()
    cycle_node = solution.detectCycle(head)
    if cycle_node:
        print("Cycle detected, starts at node with value:", cycle_node.val)
    else:
        print("No cycle detected.")

if __name__ == "__main__":
    main()
