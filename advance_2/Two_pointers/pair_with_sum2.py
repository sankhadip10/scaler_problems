"""
Problem Description:
Given a sorted array of integers (not necessarily distinct) A and an integer B, find and return how many pairs of integers (A[i], A[j]) such that i != j have sum equal to B.

Since the number of such pairs can be very large, return the number of such pairs modulo (10^9 + 7).

Problem Constraints:
1 <= |A| <= 100000
1 <= A[i] <= 10^9
1 <= B <= 10^9

Input Format:
The first argument given is the integer array A.
The second argument given is integer B.

Output Format:
Return the number of pairs for which sum is equal to B modulo (10^9+7).

Example Input:
Input 1:
A = [1, 1, 1]
B = 2

Input 2:
A = [1, 5, 7, 10]
B = 8

Example Output:
Output 1:
3

Output 2:
1

Example Explanation:
Explanation 1:
The pairs of A[i] and A[j] which sum up to 2 are (0, 1), (0, 2) and (1, 2). There are 3 pairs.

Explanation 2:
There is only one pair, such that i = 0, and j = 2 sums up to 8.
"""

# +++++++++++++++++++++++++++++++++++++BRUTE FORCE+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# class solution:
#     def solve(self,A,B):
#         n = len(A)
#         count  =0
#         for i in range(n):
#             for j in range(i+1,n):
#                 if A[i] + A[j] ==  B:
#                     count += 1
#         return count
#
# s = solution()
# A = [([1, 1, 1],2),([1,5,7,10],8)]
# for i,j in A:
#     res=s.solve(i,j)
#     print(res)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# class solution:
#     def solve(self,A,B):
#         freq  = {}
#         for num in A:
#             freq[num] = freq.get(num,0)+1
#         count  = 0
#         mod  =  10 ** 9 + 7
#
#         for num in freq:
#             complement = B - num
#             if complement in freq:
#                 if complement ==  num:
#                 # If the element is its own complement (e.g., for sum = 2B),
#                 # choose 2 out of freq[num] elements (freq[num] choose 2)
#                     count += freq[num] * (freq[num] - 1) // 2
#                 else:
#                     # For distinct pairs, multiply the frequencies
#                     count += freq[num] * freq[complement]
#                 freq[complement] = 0
#             count %= mod
#         return count
#
# s = solution()
# A = [([1, 1, 1],2),([1,5,7,10],8)]
# for i,j in A:
#     res=s.solve(i,j)
#     print(res)
#
# t.c-o(n)
# s.c-o(n)

# ======================================================================================================
class Solution:
    def solve(self, A, B):
        i = 0
        j = len(A) - 1
        n = len(A)
        count = 0
        MOD = 10 ** 9 + 7
        while i < j:
            k = A[i] + A[j]
            if k < B:
                i += 1
            elif k > B:
                j -= 1
            else:
                if A[i] == A[j]:
                    freq = j - i + 1
                    count += freq * (freq - 1) // 2
                    i = j  # Ensuring the loop will terminate
                else:
                    c1 = c2 = 0
                    x = A[i]
                    while i < n and A[i] == x:
                        i += 1
                        c1 += 1
                    y = A[j]
                    while j >= 0 and A[j] == y:
                        j -= 1
                        c2 += 1
                    count += c1 * c2
        return count % MOD


def main():
    # Example usage
    s = Solution()

    # Example 1
    A = [1, 2, 3, 4, 5]
    B = 5
    print(f"Number of pairs summing to {B} in {A}: {s.solve(A, B)}")

    # Example 2
    A = [2, 2, 3, 4, 4, 5, 6, 7, 10]
    B = 8
    print(f"Number of pairs summing to {B} in {A}: {s.solve(A, B)}")


if __name__ == "__main__":
    main()
