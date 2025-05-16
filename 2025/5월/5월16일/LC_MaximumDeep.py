# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        return self.dfs(root, 0)
    
    def dfs (self,node,depth) : 
        if node is None : 
            return depth
        left_depth = self.dfs(node.left, depth + 1)  
        right_depth = self.dfs(node.right, depth + 1) 

        return max(left_depth,right_depth)
        