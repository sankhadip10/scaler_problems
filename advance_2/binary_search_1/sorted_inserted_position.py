# # Problem Description
#
# You are given a sorted array A of size N and a target value B.
# Your task is to find the index (0-based indexing) of the target value in the array.
#
# - If the target value is present, return its index.
# - If the target value is not found, return the index of
# least element greater than or equal to B.
# - If the target value is not found and the least number greater than or equal to the target is also not present, return the length of the array (i.e., the position where the target can be placed).
# - Your solution should have a time complexity of O(log(N)).
#
# ## Problem Constraints
#
# - 1 <= N <= 10^5
# - 1 <= A[i] <= 10^5
# - 1 <= B <= 10^5
#
# ## Input Format
#
# The first argument is an integer array A of size N.
# The second argument is an integer B.
#
# ## Output Format
#
# Return an integer denoting the index of the target value.
#
# ## Example Input
#
# Input 1:
# ```
# A = [1, 3, 5, 6]
# B = 5
# ```
# Input 2:
# ```
# A = [1, 4, 9]
# B = 3
# ```
#
# ## Example Output
#
# Output 1:
# 2
# Output 2:
# 1
# ## Example Explanation
#
# Explanation 1:

# The target value is present at index 2.
#
# Explanation 2:
#
# The target value should be inserted at index 1.


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def searchInsert(self, A, B):
        # for i in range(len(A)):
        #     if A[i] == B:
        #         return i

        #     if A[i] > B:
        #         return i

        # return len(A)
        # T.C -o(n)

        left, right = 0, len(A) - 1
        ans = len(A)
        while left <= right:
            mid = left + (right - left) // 2
            if A[mid] == B:
                return mid
            elif A[mid] < B:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1
        return ans

        # t.C - o(nlogn)
        # s.c - o(1)
if __name__ == "__main__":
    # Example test cases
    A1 = [1, 3, 5, 6]
    B1 = 5
    solution = Solution()
    print(solution.searchInsert(A1, B1))  # Output: 2

    A2 = [1, 4, 9]
    B2 = 3
    print(solution.searchInsert(A2, B2))  # Output: 1

