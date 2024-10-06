# Question-------------- 

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# solution 1-------

class Solution(object):
    def twoSum(self, nums, target):
       
        lookup = {}
        
        for i, num in enumerate(nums):
            diff = target - num  
            if diff in lookup:  
                return [lookup[diff], i]
            lookup[num] = i

# solution 2-------

class Solution(object):
    def twoSum(self, nums, target):

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]