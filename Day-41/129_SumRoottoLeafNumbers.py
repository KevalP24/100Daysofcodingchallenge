# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, ans):
        if not root:
            return 0
        ans = ans * 10 + root.val
        
        if not root.left and not root.right:
            return ans
        
        ls = self.solve(root.left, ans)
        rs = self.solve(root.right, ans)
        
        return ls + rs
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum=0
        return self.solve(root, sum)
        
