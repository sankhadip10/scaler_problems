# Problem Description
# Given an integer array A of size N.
# You have to delete one element such that the GCD(Greatest common divisor) of the
# remaining array is maximum.
#
# Find the maximum value of GCD.
#
#
#
# Problem Constraints
# 2 <= N <= 105
# 1 <= A[i] <= 109
#
#
#
# Input Format
# First argument is an integer array A.
#
#
#
# Output Format
# Return an integer denoting the maximum value of GCD.
#
# Example Input
# Input 1:
# 
#  A = [12, 15, 18]
# Input 2:
#
#  A = [5, 15, 30]
#
#
# Example Output
# Output 1:
#
#  6
# Output 2:
#
#  15
#
#
# Example Explanation
# Explanation 1:
#
#  If you delete 12, gcd will be 3.
#  If you delete 15, gcd will be 6.
#  If you delete 18, gcd will 3.
#  Maximum value of gcd is 6.
# Explanation 2:
#
#  If you delete 5, gcd will be 15.
#  If you delete 15, gcd will be 5.
#  If you delete 30, gcd will be 5.
#  Maximum value of gcd is 15.

#Brute Force
class Solution:
    def gcd(self,a , b):
        while b:
            a,b = b,a%b
        return a

    def find_max_gcd(self,arr):
        global temp
        n = len(arr)
        max_gcd = 0

        for i in range(n):
            #create a new list excluding the ith element
            temp = arr[:i]+arr[i+1:]  #arr[:i] means excluding i and arr[i+1:] means including i+1

        current_gcd = temp[0]

        #Find th egcd of the new temp array
        for j in range(1,len(temp)):
            current_gcd = self.gcd(current_gcd,temp[j])


        max_gcd = max(current_gcd,max_gcd)

        return max_gcd

s = Solution()

# Test the function with a small example
print("Final Maximum GCD:", s.find_max_gcd([12, 15, 18,20]))


# TimeComplexity:O(n2)

