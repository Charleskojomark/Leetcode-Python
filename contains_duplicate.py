# 217. Contains Duplicate
# Easy
# Topics
# Companies
# Given an integer array nums, return true if any value appears at least twice in the array, 
# and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.

# Example 2:

# Input: nums = [1,2,3,4]

# Output: false

# Explanation:

# All elements are distinct.

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]

# Output: true

 

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

# def containsDuplicate(self, nums):

from typing import List

def contains_duplicate(nums: List[int]) -> bool:
    new_set = set(nums)
    if len(nums) == len(new_set):
        return False
    return True

nums = [1,2,3,1]

print(contains_duplicate(nums))

def contains_duplicate_v2(nums: List[int]) -> bool:
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
            return True
        else:
            count[num] = 1
    return False
print(contains_duplicate_v2(nums))

