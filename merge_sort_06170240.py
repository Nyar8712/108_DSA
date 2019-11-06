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
        small = nums[:divide]
        large = nums[divide:]
        
        m, p, q = 0, 0, 0
        
        while p < len(small) and q < len(large):
            if small[p] < large[q]:
                nums[m] = small[p]
                p = p+1
            else:
                nums[m] = large[q]
                q = q+1
            m = m+1

        while p < len(small):
            nums[m] = small[p]
            p = p+1
            m = m+1

        while q < len(large):
            nums[m]=large[q]
            q = q+1
            m = m+1
        return nums


# In[46]:


output = Solution().merge_sort([3,4,5,8,1,2,5,7])
output


# In[ ]:




