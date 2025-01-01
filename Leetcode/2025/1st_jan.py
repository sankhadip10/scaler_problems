"""
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e., left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

Example 1:
Input: s = "011101"
Output: 5
Explanation:
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5
left = "01" and right = "1101", score = 1 + 3 = 4
left = "011" and right = "101", score = 1 + 2 = 3
left = "0111" and right = "01", score = 1 + 1 = 2
left = "01110" and right = "1", score = 2 + 1 = 3

Example 2:
Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5

Example 3:
Input: s = "1111"
Output: 3
Explanation: The optimal split is left = "111" and right = "1", yielding a score of 0 + 3 = 3

Constraints:
2 <= s.length <= 500
The string s consists of characters '0' and '1' only.
"""
class Solution:
    def maxScore(self,s:str)->int:
        max_score = 0
        n = len(s)
        for i in range(1,n):
            left = s[:i]
            right = s[i:]
            zeros = left.count('0')
            ones = right.count('1')
            current_score = zeros + ones

            if current_score > max_score:
                max_score = current_score
        return max_score

S = Solution()
print(S.maxScore("11100"))

# Time Complexity Analysis:
#
# Outer Loop: Runs n-1 times (from 1 to n-1).
#
# Inner Operations:
#
# s[:i] and s[i:]: Slicing operations which take O(n) time in the worst case.
#
# left.count('0') and right.count('1'): Each count operation takes O(n) time.
#
# Thus, the overall time complexity is O(n * n) = O(n^2). For n = 500,
# this results in
# 250,000 operations, which is manageable but not optimal.

# Space Complexity Analysis:

# The space used is primarily for storing the substrings left and right, which in the worst case could be O(n).


class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = s.count('1')
        zeros_left = 0
        ones_right = total_ones
        max_score = 0

        #s = "11100"
        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros_left += 1
            else:
                ones_right -= 1

            current_score = zeros_left + ones_right
            if current_score > max_score:
                max_score = current_score

        return max_score


s = Solution()
print(s.maxScore("11100"))
# Time Complexity Analysis:
#
# Precomputing Total '1's: O(n).
#
# Single Iteration through the string: O(n).
#
# Thus, the overall time complexity is O(n), which is a significant improvement over the brute force approach.
#
# Space Complexity Analysis:
#
# We're using a constant amount of extra space (total_ones, zeros_left, ones_right, max_score), so the space complexity is O(1).
# https://chat.deepseek.com/a/chat/s/5c485171-f3ff-42ce-86de-09bfdf2cfe41