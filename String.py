# Leetcode Problem: 1768. Merge Strings Alternately
# Difficulty: Easy
# Approach: Two Pointers
# Time Complexity: O(m+n) where m and n are the lengths of the two strings
# Space Complexity: O(m+n) for the result string

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        result = []

        while i < m or j < n:
            if i < m:
                result += word1[i]
                i += 1
            if j < n:
                result += word2[j]
                j += 1

        return "".join(result)     
    
# Test Cases
obj = Solution()
print(obj.mergeAlternately("abc", "pqr"))
print(obj.mergeAlternately("ab", "pqrs"))
print(obj.mergeAlternately("abcd", "pq"))


# Leetcode Problem: 1071. Greatest Common Divisor of Strings
# Difficulty: Easy    Topic: String, Math
# time complexity, space complexity: O(n + m) where n and m are the lengths of the two strings

from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if they have non-zero GCD string.
        if str1 + str2 != str2 + str1:
            return ""

        # Get the GCD of the two lengths.
        max_length = gcd(len(str1), len(str2))
        return str1[:max_length]        

obj = Solution()
print(obj.gcdOfStrings("ABCABC", "ABC"))    
    
    
# Leetcode Problem: 1431. Kids With the Greatest Number of Candies
# Difficulty: Easy    Topic: String, Math   
# time complexity: O(n) where n is the number of kids, space complexity: O(n) for the result list

from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        # Find the greatest number of candies among all the kids.
        maxCandies = max(candies)
        # For each kid, check if they will have greatest number of candies among all the kids.
        result = []
        for i in range(len(candies)):
            result.append(candies[i] + extraCandies >= maxCandies)
        return result

obj = Solution()
print(obj.kidsWithCandies([2,3,5,1,3], 3))



# Leetcode Problem: 345. Reverse Vowels of a String
# Difficulty: Easy    Topic: String, Two Pointers   
# time complexity: O(n) where n is the length of the string, space complexity: O(n) for the result string

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)
        left, right = 0, len(s) -1

        while left < right:
            while left < right and s[left] not in vowels:
                left += 1

            while left < right and s[right] not in vowels:
                right -= 1

            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

        return "".join(s)
    
obj = Solution()
print(obj.reverseVowels("hello"))   
print(obj.reverseVowels("leetcode"))