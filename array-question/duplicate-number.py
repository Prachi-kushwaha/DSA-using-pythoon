# link for question --> https://leetcode.com/problems/find-the-duplicate-number/description/






# Find the Duplicate Number


# # --------------------question statement-----------------
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

 

# -------------------solution---------------------

# Brute force approach

def findDuplicate(nums):
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return nums[i]



#  Floyd's Tortoise and Hare (Cycle Detection) algorithm.

class Solution(object):
    def findDuplicate(self, nums):
            
        tortoise = nums[0]
        hare = nums[0]
        
        while True:
            tortoise = nums[tortoise]  
            hare = nums[nums[hare]]  
            if tortoise == hare:
                break
        
       
        tortoise = nums[0] 
        while tortoise != hare:
            tortoise = nums[tortoise] 
            hare = nums[hare]
        
        return hare
    
        
            