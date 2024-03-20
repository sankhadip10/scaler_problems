"""
Problem Description
Given N non-negative integers A[0], A[1], ..., A[N-1] , where each represents a point at coordinate (i, A[i]).

N vertical lines are drawn such that the two endpoints of line i is at (i, A[i]) and (i, 0).

Find two lines, which together with x-axis forms a container, such that the container contains the most water. You need to return this maximum area.

Note: You may not slant the container. It is guaranteed that the answer will fit in integer limits.

Problem Constraints
1 <= N <= 105

1 <= A[i] <= 105

Input Format
Single Argument representing a 1-D array A.

Output Format
Return single Integer denoting the maximum area you can obtain.

Example Input
Input 1:

A = [1, 5, 4, 3]
Input 2:

A = [1]

Example Output
Output 1:

6
Output 2:

0

Example Explanation
Explanation 1:

5 and 3 are distance 2 apart. So size of the base = 2. Height of container = min(5, 3) = 3.
So total area = 3 * 2 = 6
Explanation 2:

No container is formed.
"""

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# class solution:
#     def max_water(self,A):
#         #considering all pairs
#         min_value =-float('inf')
#         n = len(A)
#         if n == 1:
#             return 0
#         for i in range(len(A)):
#             for j in range(i+1,len(A)):
#                 water_accumulated = (j - i)*min(A[i],A[j])
#                 min_value =  max(min_value,water_accumulated)
#         return min_value
#
# s = solution()
# A = [1, 5, 4, 3]
# res = s.max_water(A)
# print(res)

# T.c  =o(n2)
# s.c =O(1)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        n = len(A)
        i = 0
        j = n - 1
        ans = 0
        while (i < j):
            water_accumulated = (j - i) * min(A[i], A[j])
            ans = max(ans, water_accumulated)
            if (A[i] < A[j]):
                i += 1
            else:
                j -= 1
        return ans


# Main function to test the Solution class
if __name__ == "__main__":
    # Create a Solution object
    sol = Solution()

    # Example array
    A = [1, 5, 4, 3]

    # Call the method and print the result
    result = sol.maxArea(A)
    print(result)
