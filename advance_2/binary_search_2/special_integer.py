"""
    Problem Description:

    Given an array of integers A and an integer B, find and return the maximum value K such that there is no subarray in A of size K with the sum of elements greater than B.

    Problem Constraints:

    1 <= |A| <= 100000
    1 <= A[i] <= 10^9
    1 <= B <= 10^9

    Input Format:

    The first argument given is the integer array A.
    The second argument given is integer B.

    Output Format:

    Return the maximum value of K (subarray length).

    Example Input:

    Input 1:
    A = [1, 2, 3, 4, 5] B = 10
    Input 2:
    A = [5, 17, 100, 11] B = 130

    Example Output:

    Output 1:
    2
    Output 2:
    3

    Example Explanation:

    Explanation 1:

    For K = 5, There are subarrays [1, 2, 3, 4, 5] which has a sum > B
    For K = 4, There are subarrays [1, 2, 3, 4], [2, 3, 4, 5] which has a sum > B
    For K = 3, There is a subarray [3, 4, 5] which has a sum > B
    For K = 2, There were no subarray which has a sum > B.
    Constraints are satisfied for maximal value of 2.

    Explanation 2:

    For K = 4, There are subarrays [5, 17, 100, 11] which has a sum > B
    For K = 3, There were no subarray which has a sum > B.
    Constraints are satisfied for maximal value of 3.
    """

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BRUTE FORCE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return an integer
#     def solve(self, A, B):
#         n = len(A)
#         mak_k = 0
#         for k in range(1, n + 1):
#             window_sum = sum(A[:k])
#             if window_sum > B:
#                 break
#
#             valid = True
#             for i in range(1, n - k + 1):
#                 window_sum = window_sum - A[i - 1] + A[i + k - 1]
#                 if window_sum > B:
#                     valid = False
#                     break
#
#             if valid:
#                 mak_k = k
#
#         return mak_k
#
#         # T.c~o(n2)
#
#
# def main():
#     # Input list A
#     A = list(map(int, input("Enter the list of integers (space-separated): ").split()))
#
#     # Input value B
#     B = int(input("Enter the value B: "))
#
#     solution = Solution()
#     result = solution.solve(A, B)
#     print("Maximum subarray length:", result)
#
#
# if __name__ == "__main__":
#     main()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~BRUTE FORCE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Solution:
    def solve(self, A, B):
        l = 0
        r = len(A)
        res = 0
        while l <= r:
            mid = l + (r - l) // 2
            if self.checkwindow(A, B, mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        return res

    def checkwindow(self, A, B, mid):
        sum_val = 0
        for i in range(mid):
            sum_val += A[i]

        max_sum = sum_val
        for i in range(mid, len(A)):
            sum_val = sum_val + A[i] - A[i - mid]
            max_sum = max(max_sum, sum_val)
        return max_sum <= B

# Example usage
A = [1, 4, 3, 2, 6, -1, 3, 5]
B = 13

solution = Solution()
result = solution.solve(A, B)
print(result)  # Output: 4
