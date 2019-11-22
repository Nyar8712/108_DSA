#!/usr/bin/env python
# coding: utf-8

# In[147]:


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
class Solution(object):
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root.val == val:
            if root.left == None:
                root.left = TreeNode(val)
            else:
                root.left = TreeNode(val)
                TreeNode(val).left = root.left
            return root.left
        elif val < root.val:
            if root.left:
                return Solution().insert(root.left,val)
            else:
                root.left = TreeNode(val)
                return root.left
        else:
            if root.right:
                return Solution().insert(root.right,val)
            else:
                root.right = TreeNode(val)
                return root.right
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
        
        if root == None: 
            return root 
        if target < root.val:
            root.left = Solution().delete(root.left, target)
        elif target > root.val:
            root.right = Solution().delete(root.right, target)
        else:
            if root.left == None : 
                temp = root.right  
                root = None 
                return temp  
              
            elif root.right == None : 
                temp = root.left  
                root = None
                return temp
            temp = Solution().minNode(root.right) 
            root.val = temp.val
            root.right = Solution().delete(root.right, temp.val)
        return root 
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if target < root.val:
            if root.left == None:
                return None
            else:
                return Solution().search(root.left, target)
        elif target > root.val:
            if root.right == None:
                return None
            else:
                return Solution().search(root.right, target)
        else:
            return root
    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
        if target == None:
            return root
        elif target != None:
            Solution().insert(root, new_val)
            return Solution().delete(root, target)
    def minNode(self, root):
        node = root
        while(node.left != None):
            node = node.left
        return node
    def preorder(self, root):
        if root:
            print (str(root.val))
            if root.left:
                Solution().preorder(root.left)
            if root.right:
                Solution().preorder(root.right)


# In[149]:


root = TreeNode(5)
opt = Solution().insert(root, 2)
opt = Solution().insert(root, 9)
opt = Solution().insert(root, 2)
opt = Solution().insert(root, 9)
opt = Solution().modify(root, 2, 3)
opt = Solution().search(root, 2)
print(opt)
Solution().preorder(root)


# In[ ]:




