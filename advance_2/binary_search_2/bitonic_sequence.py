# Problem Description:
# Given a bitonic sequence A of N distinct elements, write a program to find a given element B in
# the bitonic sequence in O(logN) time.
#
# NOTE:
# - A Bitonic Sequence is a sequence of numbers which is first strictly increasing then after a point strictly decreasing.
# - The sequence will have a single bitonic point where the sequence switches from increasing to decreasing.
#
# Problem Constraints:
# - 3 <= N <= 10^5
# - 1 <= A[i], B <= 10^8
# - Given array always contains a bitonic point.
# - Array A always contains distinct elements.
#
# Input Format:
# - First argument is an integer array A denoting the bitonic sequence.
# - Second argument is an integer B.
#
# Output Format:
# - Return a single integer denoting the position (0 index based) of the element B in the array A.
#   If B doesn't exist in A, return -1.
#
# Example Input:
# Input 1:
#  A = [3, 9, 10, 20, 17, 5, 1]
#  B = 20
# Input 2:
#  A = [5, 6, 7, 8, 9, 10, 3, 2, 1]
#  B = 30
#
# Example Output:
# Output 1:
#  3
# Output 2:
#  -1
#
# Example Explanation:
# Explanation 1:
#  B = 20 present in A at index 3
# Explanation 2:
#  B = 30 is not present in A

# Note: The solution should implement a binary search approach to find the bitonic point and then
# to search for the element B in O(logN) time complexity.
# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
#         for i in range(len(A)):
#             if A[i] == B:
#                 return i
#         return -1
#
# def main():
#     A = [1, 5, 3, 8, 2]
#     B = 3  # Value to find
#
#     solution = Solution()
#     index = solution.solve(A, B)
#
#     if index != -1:
#         print(f"Element {B} found at index {index}")
#     else:
#         print(f"Element {B} not found in the list")
#
# if __name__ == "__main__":
#     main()
