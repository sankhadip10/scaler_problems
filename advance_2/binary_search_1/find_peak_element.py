# Problem Description:
# Given an array of integers A, find and return the peak element in it.
# An array element is considered a peak if it is not smaller than its neighbors.
# For corner elements, we need to consider only one neighbor.
#
# NOTE:
# It is guaranteed that the array contains only a single peak element.
# Users are expected to solve this in O(log(N)) time. The array may contain duplicate elements.
#
# Problem Constraints:
# 1 <= |A| <= 100000
# 1 <= A[i] <= 10^9
#
# Input Format:
# The only argument given is the integer array A.
#
# Output Format:
# Return the peak element.
#
# Example Input:
# Input 1:
# A = [1, 2, 3, 4, 5]
# Input 2:
# A = [5, 17, 100, 11]
#
# Example Output:
# Output 1:
# 5
# Output 2:
# 100
#
# Example Explanation:
# Explanation 1:
# 5 is the peak.
# Explanation 2:
# 100 is the peak.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class Solution:
    # @param A : list of integers
    # @return an integer
#     def solve(self, A):
#         ans = float('-inf')
#         for i in range(len(A)):
#             if A[i] > ans:
#                 ans = A[i]
#         return ans
#
#
# # Main function
# def main():
#     A1 = [1, 2, 3, 4, 5]
#     A2 = [5, 17, 100, 11]
#
#     solution = Solution()
#     print(solution.solve(A1))  # Output: 5
#     print(solution.solve(A2))  # Output: 100
#
#
# if __name__ == "__main__":
#     main()
# T.C~~o(n)
# ________________________________________________________________________________________
class Solution:
    def solve(self, A):
        n = len(A)
        l = 0
        r = len(A) - 1
        if n == 1:
            return A[0]
        if A[0] > A[1]:
            return A[0]
        if A[n - 1] >= A[n - 2]:
            return A[n - 1]
        while l <= r:
            mid = l + (r - l) // 2
            if A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
                return A[mid]
            elif A[mid] > A[mid - 1]:
                l = mid + 1
            else:
                r = mid - 1


# Main function
def main():
    A1 = [1, 2, 3, 4, 5]
    A2 = [5, 17, 100, 11]

    solution = Solution()
    print(solution.solve(A1))  # Output: 5
    print(solution.solve(A2))  # Output: 100


# Time complexity: O(log(N)), where N is the number of elements in the array A.
# Space complexity: O(1), as the space used by the algorithm does not depend on the size of the input array.

if __name__ == "__main__":
    main()
