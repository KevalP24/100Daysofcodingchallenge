# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, curr, isLeft):
        if not curr:
            return 0
        
        if not curr.left and not curr.right and isLeft:
            return curr.val
        
        return self.solve(curr.left, True) + self.solve(curr.right, False)

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.solve(root, False)
