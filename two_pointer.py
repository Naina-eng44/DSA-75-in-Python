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



# Leetcode 392. Is Subsequence
# Difficulty: Easy    Topic: Two Pointers, String
# Time complexity: O(n) where n is the length of string t, space complexity: O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
    
# Example usage:
obj = Solution()
print(obj.isSubsequence("ace", "abcde"))  # Output: True
print(obj.isSubsequence("aec", "abcde"))  # Output: False



# Leetcode 11. Container With Most Water
# Difficulty: Medium    Topic: Array, Two Pointers  
# Time complexity: O(n) where n is the length of the array, space complexity: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1

        maximum = 0

        while left < right:
            width = right - left
            area = min(height[left], height[right]) * width
            maximum = max(maximum, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maximum

obj = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(obj.maxArea(height))  # Output: 49



# Leetcode 15. 3Sum
# Difficulty: Medium    Topic: Array, Two Pointers
# Time complexity: O(n^2) where n is the length of the array, space complexity: O(1) if we don't consider the output list.
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result
    
obj = Solution()
nums = [-1, 0, 1, 2, -1, -4]
print(obj.threeSum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]