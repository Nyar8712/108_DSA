#!/usr/bin/env python
# coding: utf-8

# In[45]:


class Solution(object):
    def merge_sort(self,nums):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """
        self.nums = nums
        
        if len(nums) <= 1:
            return nums
        divide = len(nums) // 2
        left = nums[:divide]
        right = nums[divide:]
        
        merge_sort(left)
        merge_sort(right)
        
        m, p, q = 0, 0, 0
        
        while p < len(left) and q < len(right):
            if left[p] < right[q]:
                nums[m] = left[p]
                p = p+1
            else:
                nums[m] = right[q]
                q = q+1
            m = m+1

        while p < len(left):
            nums[m] = left[p]
            p = p+1
            m = m+1

        while q < len(right):
            nums[m]=right[q]
            q = q+1
            m = m+1
        return nums


# In[46]:


output = Solution().merge_sort([3,4,5,8,1,2,5,7])
output


# In[ ]:




