"""
Q1. Longest Consecutive Sequence

Problem Description:
Given an unsorted integer array A of size N.
Find the length of the longest set of consecutive elements from array A.

Problem Constraints:
1 <= N <= 10^6
-10^6 <= A[i] <= 10^6

Input Format:
First argument is an integer array A of size N.

Output Format:
Return an integer denoting the length of the longest set of consecutive elements from the array A.

Example Input:
Input 1: A = [100, 4, 200, 1, 3, 2]
Input 2: A = [2, 1]

Example Output:
Output 1: 4
Output 2: 2

Example Explanation:
Explanation 1: The set of consecutive elements will be [1, 2, 3, 4].
Explanation 2: The set of consecutive elements will be [1, 2].
"""
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# class solution:
#     def longestConsecutive(self, A):
#         if not A:
#             return 0
#
#         A.sort()
#         current_streak = 1
#         longest_streak = 1
#         for i  in range(1,len(A)):
#             if A[i] != A[i-1]:
#                 if A[i] == A[i-1] +1:
#                     current_streak += 1
#                 else:
#                     longest_streak = max(longest_streak,current_streak)
#                     current_streak = 1
#
#         return  max(longest_streak,current_streak)
#
# A = [100, 4, 200, 1, 3, 2]
# s = solution()
# res = s.longestConsecutive(A)
# print(res)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# class sol:
#     def longest_consecutive(self, A):
#         n = len(A)
#         longest_streak = 0
#         for i in range(n):
#             # 0,1,1,2,6,1
#             for j in range(n):
#                 current_num = A[i]
#                 cur_streak = 1
#                 while current_num + 1 in A:
#                     current_num += 1
#                     cur_streak += 1
#                     if cur_streak > longest_streak:
#                         longest_streak = cur_streak
#         return longest_streak
#
#
# A = [100, 4, 200, 1, 3, 2]
# s = sol()
# res = s.longest_consecutive(A)
# print(res)

# t.c----o(n2)*k
# s.c -o(n)
# -------------------------------------------------------------------------------------------------------
# class sol:
#     def longestConsequtive(self,A):
#         A = list(set(A))
#         longest_streak = 1
#         n = len(A)
#         for i in range(len(A)):
#             current_sum =  A[i]
#             current_streak = 1
#             while current_sum + 1 in A:
#                 current_streak += 1
#                 current_sum = current_sum + 1
#
#                 if current_streak > longest_streak:
#                     longest_streak =  current_streak
#
#         return longest_streak
#
# A = [100, 4, 200, 1, 3, 2]
# s = sol()
# res = s.longestConsequtive(A)
# print(res)
#
# t.c -o(n2)
# s.c - o(n)
# ______________________________________________________________________________________________________
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        num_set = set(A)
        max_length = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                length = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    length += 1

                max_length = max(max_length, length)

        return max_length


def main():
    # Example usage
    A = [100, 4, 200, 1, 3, 2]
    solution = Solution()
    result = solution.longestConsecutive(A)
    print("The length of the longest consecutive elements sequence is:", result)


if __name__ == "__main__":
    main()

# t.c =o(n)
# s.c=o(n)