# Problem Description
#
# You are given two positive numbers A and B . You need to find the maximum valued integer X such that:
#
# X divides A i.e. A % X = 0
# X and B are co-prime i.e. gcd(X, B) = 1
#
#
# Problem Constraints
#
# 1 <= A, B <= 109
#
#
#
# Input Format
#
# First argument is an integer A.
# Second argument is an integer B.
#
#
#
# Output Format
#
# Return an integer maximum value of X as descibed above.
#
#
#
# Example Input
#
# Input 1:
#
#  A = 30
#  B = 12
# Input 2:
#
#  A = 5
#  B = 10
#
#
# Example Output
#
# Output 1:
#
#  5
# Output 2:
#
#  1
#
#
# Example Explanation
#
# Explanation 1:
#
#  All divisors of A are (1, 2, 3, 5, 6, 10, 15, 30).
#  The maximum value is 5 such that A%5 == 0 and gcd(5,12) = 1
# Explanation 2:
#
#  1 is the only value such that A%5 == 0 and gcd(1,10) = 1
#
#
# Expected Output
# Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
class Solution:
    def gcd(self,a,b):
        while b:
            a,b = b, a%b
        return a

    def cpFact(self,A,B):
        while True:
            p = self.gcd(A,B)
            if p == 1:
                break
            A = A // p
        return A


s =Solution()
a=s.cpFact(300,25)
print(a)

# t.c-O(logmin(A,B)) per iteration on the loop