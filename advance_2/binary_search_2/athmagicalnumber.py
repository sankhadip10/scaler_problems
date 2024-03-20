# Given three positive integers A, B, and C.
# A positive integer is magical if divisible by either B or C.
# Return the Ath smallest magical number. Return modulo 10^9 + 7 to prevent integer overflow.

# Constraints:
# 1 <= A <= 10^9
# 2 <= B, C <= 40000

# Function Signature:
# def solve(A: int, B: int, C: int) -> int:

# Example:
# Input:
# A = 1, B = 2, C = 3
# Output:
# 2
# Explanation:
# The 1st magical number is 2.

# Input:
# A = 4, B = 2, C = 3
# Output:
# 6
# Explanation:
# The first four magical numbers are 2, 3, 4, 6, so the 4th magical number is 6.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#BRUTE FORCE
# class Solution:
#     # @param A : integer
#     # @param B : integer
#     # @param C : integer
#     # @return an integer
#     def solve(self, A, B, C):
#         count = 0
#         num = 0
#         while count < A:
#             num += 1
#             if num % B == 0 or num % C == 0:
#                 count += 1
#         return num
#
# # Example usage:
# sol = Solution()
# A = 5
# B = 2
# C = 4
# print(sol.solve(A, B, C))  # Output: 10
# t.c~o(A)
# s.c~o(1)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~