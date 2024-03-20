# Problem Description:
# Given a sorted array of integers A of size N and an integer B,
# where array A is rotated at some pivot unknown beforehand.
#
# For example, the array [0, 1, 2, 4, 5, 6, 7] might become [4, 5, 6, 7, 0, 1, 2].
#
# Your task is to search for the target value B in the array. If found, return its index; otherwise, return -1.
#
# You can assume that no duplicates exist in the array.
#
# NOTE: You are expected to solve this problem with a time complexity of O(log(N)).
#
# Problem Constraints:
# 1 <= N <= 1000000
# 1 <= A[i] <= 109
# All elements in A are Distinct.
#
# Input Format:
# The First argument given is the integer array A.
# The Second argument given is the integer B.
#
# Output Format:
# Return index of B in array A, otherwise return -1
#
# Example Input:
# Input 1:
# A = [4, 5, 6, 7, 0, 1, 2, 3]
# B = 4
# Input 2:
# A : [ 9, 10, 3, 5, 6, 8 ]
# B : 5
#
# Example Output:
# Output 1:
#  0
# Output 2:
#  3
#
# Example Explanation:
# Explanation 1:
# Target 4 is found at index 0 in A.
# Explanation 2:
# Target 5 is found at index 3 in A.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BRUTE FORCE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class Solution:
# @param A : tuple of integers
# @param B : integer
# @return an integer
#     def search(self, A, B):
#         for i in range(len(A)):
#             if A[i] == B:
#                 return i
#         return -1
#
# def main():
#     A = [4, 5, 6, 7, 0, 1, 2, 3]
#     B = 4
#     solution = Solution()
#     result = solution.search(A, B)
#     print("Index of", B, "in array A:", result)
#
#     A = [9, 10, 3, 5, 6, 8]
#     B = 5
#     result = solution.search(A, B)
#     print("Index of", B, "in array A:", result)
#
# if __name__ == "__main__":
#     main()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BRUTE FORCE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
            elif A[l] < A[mid]:  # Left half is sorted
                if A[l] <= B < A[mid]:  # Target is in the sorted left half
                    r = mid - 1
                else:  # Target is in the right half
                    l = mid + 1
            else:  # Right half is sorted
                if A[mid] < B <= A[r]:  # Target is in the sorted right half
                    l = mid + 1
                else:  # Target is in the left half
                    r = mid - 1
        return -1


def main():
    A = [4, 5, 6, 7, 0, 1, 2, 3]
    B = 1
    sol = Solution()
    result = sol.search(A, B)
    print("Index of", B, "in array A:", result)

    A = [9, 10, 3, 5, 6, 8]
    B = 5
    result = sol.search(A, B)
    print("Index of", B, "in array A:", result)


if __name__ == "__main__":
    main()


    #tc~~~o(logn)
    #sc~~~o(1)
