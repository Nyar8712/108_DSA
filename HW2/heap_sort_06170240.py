#!/usr/bin/env python
# coding: utf-8

# In[42]:


class Solution(object):
    def heap_sort(self, nums):
        if len(nums) <= 1:
            return nums
        self.nums = nums
        Solution().build_max_heap(nums)
        for i in range(len(nums) - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            Solution().heapify(nums, 0, i)
        return nums
    
    def parent(self, i):
        return (i - 1) // 2
 
    def left(self, i):
        return 2*i + 1
     
    def right(self, i):
        return 2*i + 2
 
    def build_max_heap(self, nums):
        a = Solution().parent(len(nums) - 1)
        while a >= 0:
            Solution().heapify(nums, a, len(nums))
            a -= 1
    
    def heapify(self, nums, i, n):
        l = Solution().left(i)
        r = Solution().right(i)
        if (l < n and nums[l] > nums[i]):
            largest = l
        else:
            largest = i
        if (r < n and nums[r] > nums[largest]):
            largest = r
        if (largest != i):
            nums[largest], nums[i] = nums[i], nums[largest]
            Solution().heapify(nums, largest, n)


# In[43]:


output = Solution().heap_sort([8,9,4,55,3,4,17,0,4,-3,2,-5,4])
output


# In[ ]:




