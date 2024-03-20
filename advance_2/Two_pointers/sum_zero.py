"""
Problem Description:
Jerry is excited about an array that Tom gave him. The array A consists of N integers.

Tom challenges Jerry to find all such unique triplets a, b, c in A such that a + b = -c.

Note:
- Elements in a triplet (a, b, c) must be in non-decreasing order. (i.e., a ≤ b ≤ c)
- The solution set must not contain duplicate triplets.

Problem Constraints:
0 <= N <= 7000
-10^8 <= A[i] <= 10^8

Input Format:
Single argument representing a 1-D array A.

Output Format:
Output a 2-D vector where each row represents a unique triplet.

Example Input:
Input 1:
A = [-5, 2, 1, 3]
Input 2:
A = [-1, 0, 1, 2, -1, 4]

Example Output:
Output 1:
[[-5, 2, 3]]
Output 2:
[[-1, 0, 1], [-1, -1, 2]]

Example Explanation:
Explanation 1:
Out of all the possible triplets, the triplet (-5, 2, 3) only satisfies the condition, which is in the form [(-5) + (2) = - (3)]
Explanation 2:
Out of all the possible triplets, only the above two triplets satisfy the condition and are unique.
"""

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# class solution:
#     def threeSum(self,A):
#         n = len(A)
#         res = []
#         A.sort()
#         for i in range(n):
#             if i > 0 and A[i] == A[i-1]:
#                 continue
#
#             for j in range(i+1,n):
#                 if j > i+1 and A[j] == A[j-1]:
#                     continue
#                 for k in range(j+1,n):
#                     if k>j+1 and A[k] == A[k-1]:
#                         continue
#                     if A[i]+A[j]+A[k] == 0:
#                         res.append([A[i],A[j],A[k]])
#         return res
#
# s =solution()
# A = [[-5, 2, 1, 3],[-1, 0, 1, 2, -1, 4]]
# for i in A:
#     final_list = s.threeSum(i)
#     print(final_list)

#
# Time Complexity = o(n3)
# Space complexity = o(n)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class Solution:
    def threeSum(self, A):
        n = len(A)
        A.sort()
        res = []
        for i in range(n):
            if i > 0 and A[i] == A[i-1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                total = A[i] + A[left] + A[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([A[i], A[left], A[right]])
                    while left < right and A[left] == A[left + 1]:
                        left += 1
                    while left < right and A[right] == A[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res

def main():
    # Example usage
    print("Enter the array elements separated by space:")
    A = list(map(int, input().split()))  # Read array input from user

    solution = Solution()
    triplets = solution.threeSum(A)

    print("\nUnique triplets that sum up to 0 are:")
    for triplet in triplets:
        print(triplet)

if __name__ == "__main__":
    main()
