class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        vals = []

        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return len(set(vals)) == 1
