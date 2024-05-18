# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(cur_node, parent):
            
            if cur_node == None:
                return 0
            
            ans = dfs(cur_node.left, cur_node) + dfs(cur_node.right, cur_node) 
            f_this = cur_node.val - 1 
            parent.val += f_this  
            ans += abs(f_this) 
            
            return ans
        return dfs(root, TreeNode())
