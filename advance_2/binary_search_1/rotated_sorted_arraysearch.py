# Problem Description
# Given a sorted array of integers A of size N and an integer B,
# where array A is rotated at some pivot unknown beforehand.
# Your task is to search for the target value B in the array. If found, return its index; otherwise, return -1.
# You can assume that no duplicates exist in the array.
# NOTE: You are expected to solve this problem with a time complexity of O(log(N)).

# Problem Constraints
# 1 <= N <= 1000000
# 1 <= A[i] <= 109
# All elements in A are Distinct.

# Input Format
# The First argument given is the integer array A.
# The Second argument given is the integer B.

# Output Format
# Return index of B in array A, otherwise return -1

# Example Input
# Input 1:

# A = [4, 5, 6, 7, 0, 1, 2, 3]
# B = 4
# Input 2:

# A : [ 9, 10, 3, 5, 6, 8 ]
# B : 5

# Example Output
# Output 1:

#  0
# Output 2:

#  3

# Example Explanation
# Explanation 1:

# Target 4 is found at index 0 in A.
# Explanation 2:

# Target 5 is found at index 3 in A.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class Solution:
#     # @param A : tuple of integers
#     # @param B : integer
#     # @return an integer
#     def search(self, A, B):
#         for i in range(len(A)):
#             if A[i] == B:
#                 return i
#         return -1
#
# # Example usage:
# if __name__ == "__main__":
#     sol = Solution()
#     A = [4, 5, 6, 7, 0, 1, 2, 3]
#     B = 4
#     print(sol.search(A, B))  # Output: 0
#
#     A = [9, 10, 3, 5, 6, 8]
#     B = 5
#     print(sol.search(A, B))  # Output: 3
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        l = 0
        r = len(A) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if A[mid] == B:
                return mid
            elif A[l] <= A[mid]:  # Left half is sorted
                if A[l] <= B < A[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:  # Right half is sorted
                if A[mid] < B <= A[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    A = [19, 20, 21, 22, 28, 29, 32, 36, 39, 40, 41, 42, 43, 45, 48, 49, 51, 54, 55, 56, 58, 60, 61, 62, 65, 67, 69, 71, 72, 74, 75, 78, 81, 84, 85, 87, 89, 92, 94, 95, 96, 97, 98, 99, 100, 105, 107, 108, 109, 110, 112, 113, 115, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 128, 130, 131, 133, 134, 135, 136, 137, 138, 139, 141, 142, 144, 146, 147, 148, 149, 150, 153, 155, 157, 159, 161, 163, 164, 169, 170, 175, 176, 179, 180, 185, 187, 188, 189, 192, 196, 199, 201, 203, 205, 3, 7, 9, 10, 12, 13, 17]
    B = 6
    print(sol.search(A, B))  # Output: -1
