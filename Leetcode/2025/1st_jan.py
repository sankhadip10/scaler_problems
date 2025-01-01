# s="11000"
# for i in range(len(s)):
#     left = s[:i]
#     right = s[i:]
#     print((left))
#     print((right))
#     print("+++")
class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = s.count('1')
        zeros_left = 0
        ones_right = total_ones
        max_score = 0
        for i in range(len(s) - 1):  # Stop before the last character
            if s[i] == '0':
                zeros_left += 1
            else:
                ones_right -= 1
            current_score = zeros_left + ones_right
            if current_score > max_score:
                max_score = current_score
        return max_score

s = Solution()
val=s.maxScore(s="11000")
print(val)
