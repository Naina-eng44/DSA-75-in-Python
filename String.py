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