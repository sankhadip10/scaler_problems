"""
Problem Description
The government wants to set up B distribution offices across N cities for the distribution of food packets.

The population of the ith city is A[i]. Each city must have at least 1 office and every person is assigned to exactly one office in their own city.

Let M denote the minimum number of people that are assigned to any of the offices. Find the maximum value of M possible.

Problem Constraints
1 <= N <= 10^5

1 <= A[i] <= 10^6

1 <= B <= 5 x 10^5

Input Format
The first line of input contains an integer array A.

The second line of input contains an integer B.

Output Format
Return one integer representing the maximum number of people who can get food in any single office.

Example Input
Input 1:
  A = [10000, 22000, 36000]
  B = 6
Input 2:
  A = [1, 1, 1]
  B = 4
"""

class Solution:
    def solve(self, A, B):
        ans = 0
        l = 1
        r = min(A)
        while (l <= r):
            mid = l + (r - l) // 2
            if self.check(A, mid, B):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

    def check(self, A, mid, B):
        req = 0
        for i in A:
            req += i // mid
        return req >= B


# Main function to call the solve method
if __name__ == "__main__":
    # Problem statement:
    # The government wants to set up B distribution offices across N cities for the distribution of food packets.
    # The population of the ith city is A[i]. Each city must have at least 1 office and every person is assigned to
    # exactly one office in their own city. Let M denote the minimum number of people that are assigned to any of the
    # offices. Find the maximum value of M possible. Return one integer representing the maximum number of people who
    # can get food in any single office.

    A = [8, 7, 1, 5, 5, 10, 10, 1, 5, 3]
    B = 17
    solution = Solution()
    print(solution.solve(A, B))
