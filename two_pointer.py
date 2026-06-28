# leetcode 283. Move Zeroes
# Difficulty: Easy    Topic: Array, Two Pointers
# Time complexity: O(n) where n is the length of the array, space complexity: O(1) since we are modifying the input array in place.

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index], nums[i] = nums[i], nums[index]
                index += 1
                
obj = Solution()
nums = [0,1,0,3,12]
obj.moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]