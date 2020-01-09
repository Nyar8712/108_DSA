class Solution(object):
    def twoSum(self, nums, target):
        opt=[]
        for i in nums:
            cal=nums[nums.index(i)+1:]
            a=target-i
            if a in cal:
                opt.append(nums.index(i))
                opt.append(nums.index(i)+1+cal.index(a))
                return opt
