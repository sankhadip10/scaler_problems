"""
Problem Description:
Given an integer A, compute and return the square root of A.
If A is not a perfect square, return the floor(sqrt(A)).

NOTE:
   The value of A*A can cross the range of Integer.
   Do not use the sqrt function from the standard library.
   Users are expected to solve this in O(log(A)) time.

Problem Constraints:
0 <= A <= 10^9

Input Format:
The first and only argument given is the integer A.

Output Format:
Return floor(sqrt(A))

Example Input:
Input 1:
11
Input 2:
9

Example Output:
Output 1:
3
Output 2:
3

Example Explanation:
Explanation 1:
When A = 11, the square root of A is 3.316. It is not a perfect square, so we return the floor which is 3.
Explanation 2:
When A = 9, which is a perfect square of 3, so we return 3.
"""

##########################################################################################################
# class Solution:
    # @param A : integer
    # @return an integer
#     def sqrt(self, A):
#         # Brute force
#         ans = 0
#         for i in range(1, A + 1):
#             if i * i <= A:
#                 ans = i
#         return ans
#
# def main():
#     # Create an instance of the Solution class
#     solution = Solution()
#
#     # Test cases
#     test_cases = [11, 9, 25, 0, 1, 1000000]
#
#     # Iterate through each test case
#     for A in test_cases:
#         # Call the sqrt function and print the result
#         print("Square root of", A, ":", solution.sqrt(A))
#
# # Call the main function
# if __name__ == "__main__":
#     main()

#####################################~~~~~~B R U T E    F O R C E~~~~~###################################
class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        if A == 0 or A == 1:
            return A

        l = 1
        r = A
        ans = 0
        while (l <= r):
            mid = l + (r - l) // 2
            if mid * mid == A:
                return mid
            elif mid * mid < A:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans


def main():
    # Create an instance of the Solution class
    solution = Solution()

    # Test cases
    test_cases = [11, 9, 25, 0, 1, 1000000]

    # Iterate through each test case
    for A in test_cases:
        # Call the sqrt function and print the result
        print("Square root of", A, ":", solution.sqrt(A))


# Call the main function
if __name__ == "__main__":
    main()



#tc -O(logA)
#sc - o(1)