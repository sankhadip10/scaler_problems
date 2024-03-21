# Problem Description:
# Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.
# If the given array contains a sub-array with sum zero return 1, else return 0.

# Problem Constraints:
# 1 <= |A| <= 100000
# -10^9 <= A[i] <= 10^9

# Input Format:
# The only argument given is the integer array A.

# Output Format:
# Return whether the given array contains a subarray with a sum equal to 0.

# Example Input:
# Input 1:
# A = [1, 2, 3, 4, 5]
# Input 2:
# A = [4, -1, 1]

# Example Output:
# Output 1:
# 0
# Output 2:
# 1

# Example Explanation:
# Explanation 1:
# No subarray has sum 0.
# Explanation 2:
# The subarray [-1, 1] has sum 0.

# class Solution:
#     def solve(self,A):
#         # A= [1, 2, 3, 4, 5]
#         n = len(A)
#         for i in range(n):
#             sum = 0
#             for j in range(i,n):
#                 sum += A[j]
#                 if sum == 0:
#                     return 1
#         return 0
#
# A = [4, -1, 1]
# s= Solution()
# res = s.solve(A)
# print(res)
#
# time complexity - o(n2)
# space complexity-o(1)

# =======================================================================================================
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Just write your code below to complete the function. Required input is available to you as the function arguments.
        # Do not print the result or any output. Just return the result via this function.
        prefix_sum = 0
        sum_set = set()

        for num in A:
            prefix_sum += num

            if prefix_sum == 0 or prefix_sum in sum_set:
                return 1

            sum_set.add(prefix_sum)

        return 0


def main():
    # Create an instance of the Solution class
    solution = Solution()

    # Example array of integers
    A = [4, -1, 1]

    # Call the solve method with the array and store the result
    result = solution.solve(A)

    # Print the result
    print(result)


if __name__ == "__main__":
    main()


# T,c -o(n)
# s.c-o(n)
