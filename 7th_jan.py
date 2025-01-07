# Given an array of strings `words`, return all strings in `words` that are substrings of another word.
# A substring is a contiguous sequence of characters within a string.

# Example 1:
# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is a substring of "mass" and "hero" is a substring of "superhero".
# ["hero","as"] is also a valid answer.

# Example 2:
# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et" and "code" are substrings of "leetcode".

# Example 3:
# Input: words = ["blue","green","bu"]
# Output: []
# Explanation: No string in `words` is a substring of another string.

# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 30
# words[i] contains only lowercase English letters.
# All the strings in `words` are unique.

# Write a function to solve this problem. Provide both brute force and optimized solutions,
# and explain the time and space complexity for each approach.

from typing import List
# class Solution:
#     def find_substrings_brute_force(self,words:List[str]) -> List[str]:
#         result = []
#         for i in range(len(words)):
#             for j in range(len(words)):
#                 if i!=j and words[i] in words[j]:
#                     result.append(words[i])
#                     break
#         return result

# s=Solution()
# words = ["mass", "as", "hero", "superhero"]
# print(s.find_substrings_brute_force(words))

# Time Complexity (TC):
# Let n be the number of words in the array.
#
# Let m be the average length of the words.
#
# For each word, we compare it against every other word, which takes O(n) comparisons.
#
# Each comparison involves checking if one string is a substring of another, which takes O(m^2) in the worst case (using a naive substring search).
#
# Therefore, the total time complexity is O(n^2 * m^2).

# Space Complexity (SC):
# The space complexity is O(1) if we ignore the space required for
#     the output list. If we consider the output list, it is O(k),
#     where k is the number of words that are substrings of other words




from typing import List
class Solution:
    def find_substrings_brute_force(self,words:List[str]) -> List[str]:
        words.sort(key=len)
        result = []
        word_set = set(words)

        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if words[i] in words[j]:
                    result.append(words[i])
                    break
        return result


s=Solution()
words = ["mass", "as", "hero", "superhero"]
print(s.find_substrings_brute_force(words))

# Time Complexity (TC):
# Sorting the words takes O(n log n).
#
# Checking each word against longer words takes O(n * m^2) in the worst case.
#
# Therefore, the total time complexity is O(n log n + n * m^2).
#
# Space Complexity (SC):
# The space complexity is O(n) due to the set used for storing words.