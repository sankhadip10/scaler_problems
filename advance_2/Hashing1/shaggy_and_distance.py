# Q2. Shaggy and Distances
# The task is to find a special pair in an array A of N elements
# where the elements of the pair are equal, and the distance between them is
# the minimum. Distance is defined as |i-j|. Return -1 if no such pair exists.
# Constraints: 1 <= |A| <= 105
# Input: Integer array A
# Output: Minimum distance between any special pair, or -1 if none exist
#
# Example Inputs and Outputs:
# Input: A = [7, 1, 3, 4, 1, 7]
# Output: 3
# Explanation: Minimum distance special pair is between the two 1's at indices 1 and 4.
#
# Input: A = [1, 1]
# Output: 1
# Explanation: Only one pair exists, between the two 1's at indices 1 and 2.
#
# class solution:
#     def solve(self, A):
#         n = len(A)
#         res = float('inf')
#         for i in range(n):
#             for j in range(i + 1, n):
#                 ans = 0
#                 if A[i] == A[j]:
#                     ans = abs(i - j)
#                     res = min(ans, res)
#
#         if res == float('inf'):
#             return -1
#         else:
#             return res
#
#
# A = [7, 1, 3, 4, 1, 7]
# s = solution()
# result = s.solve(A)
# print(result)

# timecomplexity -o(n2)
# space complecity-o(1)


# ------------------------------------------------------------------------------------------------------
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        freq = {}
        # for i in A:
        #     freq[i] =freq.get(i,0)+1
        ans =float('inf')
        for i in range(len(A)):
            if A[i] in freq:
                ans = min(ans,i - freq[A[i]])
                freq[A[i]] = i
            else:
                freq[A[i]] = i

        if ans == float('inf'):
            return -1
        else:
            return ans

# T.c-o(n)
# s.c-o(n)
def main():
    # Create an instance of the Solution class
    solution = Solution()

    # Define test cases
    test_cases = [
        [7, 1, 3, 4, 1, 7],
        [1, 1],
        [1, 2, 3, 4, 5],
        [9, 29, 7, 9, 29, 7]
    ]

    # Iterate through each test case and print the result
    for test_case in test_cases:
        print(f"Array: {test_case}")
        result = solution.solve(test_case)
        print(f"Minimum distance between any special pair: {result}\n")


if __name__ == "__main__":
    main()
