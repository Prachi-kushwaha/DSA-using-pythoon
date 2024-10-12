# link for question --> https://leetcode.com/problems/product-of-array-except-self/






# Product of Array Except Self

# # --------------------question statement-----------------
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 
 

# -------------------solution---------------------
# Brute force approach

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        result = []
        
        for i in range(n):
            product = 1 
             
            for j in range(n):
                if i != j: 
                    product *= nums[j]
                      
            result.append(product)
        
        return result


# 2nd solution with time complexity of O(n)

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        
        
        result = [1] * n
        
        
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
        
        right_product = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result


        