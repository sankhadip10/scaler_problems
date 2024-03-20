# Problem Statement:
# Given an one-dimensional integer array A of size N and an integer B.
# Count all distinct pairs with difference equal to B.
# Here a pair is defined as an integer pair (x, y), where x and y are both numbers in the array and their absolute difference is B.

# Problem Constraints:
# 1 <= N <= 104
# 0 <= A[i], B <= 105

# Input Format:
# First argument is an one-dimensional integer array A of size N.
# Second argument is an integer B.

# Output Format:
# Return an integer denoting the count of all distinct pairs with difference equal to B.

# Example Input:
# Input 1:
# A = [1, 5, 3, 4, 2]
# B = 3
# Input 2:
# A = [8, 12, 16, 4, 0, 20]
# B = 4
# Input 3:
# A = [1, 1, 1, 2, 2]
# B = 0

# Example Output:
# Output 1:
# 2
# Output 2:
# 5
# Output 3:
# 2

# Example Explanation:
# Explanation 1:
# There are 2 unique pairs with difference 3, the pairs are {1, 4} and {5, 2}
# Explanation 2:
# There are 5 unique pairs with difference 4, the pairs are {0, 4}, {4, 8}, {8, 12}, {12, 16} and {16, 20}
# Explanation 3:
# There are 2 unique pairs with difference 0, the pairs are {1, 1} and {2, 2}.

# =======================================================================================================
# class Solution:
#     def solve(self, A, B):
#         n = len(A)
#         count = 0
#         unique_pairs = set()
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if i!=j and abs(A[i] - A[j]) == B:
#                     unique_pairs.add(tuple((A[i],A[j])))
#         return len(unique_pairs)
#
#
# def main():
#     examples = [([1, 5, 3, 4, 2],3),([8, 12, 16, 4, 0, 20],4),([1, 1, 1, 2, 2],0)]
#     for A,B in examples:
#
#         res = Solution().solve(A, B)
#
#         print(f"result: {res} ")
#
#
# if __name__ == "__main__":
#     main()
# ---------------------------------------------------------------------------------------------------------
# class solution:
#     def solve(self,A,B):
#         element = set(A)
#         visited = set()
#         count  = 0
#
#         for x in A:
#             if x not in visited:
#                 if B>0 and (x+B in element):
#                     count += 1
#                 elif B==0 and A.count(x)>1:
#                     count += 1
#                 visited.add(x)
#         return count
# def main():
#     examples = [([1, 5, 3, 4, 2],3),([8, 12, 16, 4, 0, 20],4),([1, 1, 1, 2, 2],0)]
#     for A,B in examples:
#
#         res = solution().solve(A, B)
#
#         print(f"result: {res} ")
#
#
# if __name__ == "__main__":
#     main()

# t.c-o(n2)
# s.c -o(n)
# -------------------------------------------------------------------------------------------------------
# class solution:
#     def solve(self,A,B):
#         freq_map = {}
#         for x in A:
#             freq_map[x] = freq_map.get(0,1)+1
#         count = 0
#
#         if B>0:
#             for x in freq_map:
#                 if x+B in freq_map:
#                     count += 1
#         else:
#             for x in freq_map:
#                 if freq_map[x] > 1:
#                     count += 1
#         return count
#
# def main():
#     examples = [([1, 5, 3, 4, 2],3),([8, 12, 16, 4, 0, 20],4),([1, 1, 1, 2, 2],0)]
#     for A,B in examples:
#
#         res = solution().solve(A, B)
#
#         print(f"result: {res} ")
#
#
# if __name__ == "__main__":
#     main()

# T.c-o(n)
# s.-o(n)
# ----------------------------------------------------------------------------------------------------
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        # Initialize two pointers and sort the input array
        i = 0
        j = i + 1
        n = len(A)
        ans = 0
        A.sort()  # Sorting the array, O(n log n) time complexity

        # Iterate with two pointers to find pairs with the difference B
        while j < n:
            # Ensure j moves ahead if it's the same as i
            if (j == i):
                j += 1
                continue
            x, y = A[i], A[j]

            # When the difference matches B, increment answer and move pointers to next unique elements
            if (y - x == B):
                ans += 1
                while (i < n and A[i] == x): i += 1
                while (j < n and A[j] == y): j += 1
            elif (y - x) > B:  # Move i to reduce the difference
                i += 1
            else:  # Move j to increase the difference
                j += 1

        return ans

# Time Complexity: O(n log n) due to sorting the array. The while loop and subsequent operations within are linear, making the overall time complexity dominated by the sorting step.
# Space Complexity: O(log n) for the sorting algorithm's stack space in typical cases if the sort is done in-place. The additional variables used (i, j, n, ans, x, y) contribute a constant space overhead, O(1).
def main():
    # Instantiate the Solution class
    sol = Solution()

    # Test cases
    test_cases = [
        ([1, 5, 3, 4, 2], 3),
        ([8, 12, 16, 4, 0, 20], 4),
        ([1, 1, 1, 2, 2], 0),
        ([3, 1, 4, 1, 5], 2)  # Example where no elements are repeated
    ]

    # Loop through each test case and print the result
    for A, B in test_cases:
        result = sol.solve(A, B)
        print(f"For A = {A} and B = {B}, the number of distinct pairs is: {result}")


if __name__ == "__main__":
    main()
