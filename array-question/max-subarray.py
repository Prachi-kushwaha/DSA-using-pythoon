# link for question --> https://leetcode.com/problems/maximum-subarray/description/






# Maximum Subarray

# # --------------------question statement-----------------
# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 


 
# -------------------solution---------------------


class Solution:
    def maxSubArray(self, nums):
        
        max_current = max_global = nums[0]
        
        
        for i in range(1, len(nums)):
           
            max_current = max(nums[i], max_current + nums[i])
            
        
            if max_current > max_global:
                max_global = max_current
        
        return max_global
