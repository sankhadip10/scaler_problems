# Problem Description
# Given an integer array A of size N.
# You have to delete one element such that the GCD(Greatest common divisor) of the
# remaining array is maximum.
#
# Find the maximum value of GCD.
#
#
#
# Problem Constraints
# 2 <= N <= 105
# 1 <= A[i] <= 109
#
#
#
# Input Format
# First argument is an integer array A.
#
#
#
# Output Format
# Return an integer denoting the maximum value of GCD.
#
# Example Input
# Input 1:
#
#  A = [12, 15, 18]
# Input 2:
#
#  A = [5, 15, 30]
#
#
# Example Output
# Output 1:
#
#  6
# Output 2:
#
#  15
#
#
# Example Explanation
# Explanation 1:
#
#  If you delete 12, gcd will be 3.
#  If you delete 15, gcd will be 6.
#  If you delete 18, gcd will 3.
#  Maximum value of gcd is 6.
# Explanation 2:
#
#  If you delete 5, gcd will be 15.
#  If you delete 15, gcd will be 5.
#  If you delete 30, gcd will be 5.
#  Maximum value of gcd is 15.

#Optimize


class Solution:
    # @param A : list of integers
    # @return an integer
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def solve(self, A):
        n = len(A)
        prefix_gcd = [0] * n
        suffix_gcd = [0] * n

        # Initialize the first element of the prefix and the last element of the suffix
        prefix_gcd[0] = A[0]
        suffix_gcd[-1] = A[-1]

        # Create the prefix and suffix GCDs
        for i in range(1, n):
            prefix_gcd[i] = self.gcd(prefix_gcd[i - 1], A[i])
            suffix_gcd[n - i - 1] = self.gcd(suffix_gcd[n - i], A[n - i - 1])

        # Compute the maximum GCD after removing each element
        max_gcd = 0

        # Check for the case when the first element is removed
        max_gcd = max(max_gcd, suffix_gcd[1])

        # Check for each element except the first and last
        for i in range(1, n - 1):
            current_gcd = self.gcd(prefix_gcd[i - 1], suffix_gcd[i + 1])
            max_gcd = max(max_gcd, current_gcd)

        # Check for the case when the last element is removed
        max_gcd = max(max_gcd, prefix_gcd[n - 2])

        return max_gcd



s =Solution()
res= s.solve([7,21])

print("Final Maximum GCD:",res)