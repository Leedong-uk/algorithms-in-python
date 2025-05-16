class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(root, p, q):  # self 제거
            if root is None:
                return None
            
            if root in [p, q]:
                return root
            
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            
            if left and right:
                return root  
            
            if left and right is None : 
                return left 
            
            if right and left is None : 
                return right
        
        return dfs(root, p, q)
