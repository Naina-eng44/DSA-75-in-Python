# 605. Can Place Flowers
# Suppose you have a long flowerbed in which some of the plots are planted, 
# and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
# and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
# Time complexity: O(n) where n is the length of the flowerbed, space complexity: O(1) since we are modifying the input array in place.
# question type: array, greedy
from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            # Check if the current plot is empty.
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty.
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_plot = (i == len(flowerbed) -1) or (flowerbed[i + 1] == 0)

                # If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_plot:
                    flowerbed[i] = 1
                    count += 1

        return count >= n
# Test Cases
obj = Solution()    
print(obj.canPlaceFlowers([1,0,0,0,1], 1))
print(obj.canPlaceFlowers([1,0,0,0,1], 2))