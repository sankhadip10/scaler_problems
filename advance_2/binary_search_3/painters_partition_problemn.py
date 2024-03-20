"""
Problem Description:
Given 2 integers A and B, and an array of integers C of size N.
Element C[i] represents the length of the ith board. You have to paint all N boards [C0, C1, C2, C3 … CN-1].
There are A painters available and each of them takes B units of time to paint 1 unit of the board.

Calculate and return the minimum time required to paint all boards under the constraints that any painter will only paint contiguous sections of the board.

NOTE:
1. 2 painters cannot share a board to paint. That is to say, a board cannot be painted partially by one painter, and partially by another.
2. A painter will only paint contiguous boards. This means a configuration where painter 1 paints boards 1 and 3 but not 2 is invalid.

Return the answer % 10000003.

Problem Constraints:
1 <= A <= 1000
1 <= B <= 10^6
1 <= N <= 10^5
1 <= C[i] <= 10^6

Input Format:
The first argument given is the integer A.
The second argument given is the integer B.
The third argument given is the integer array C.

Output Format:
Return minimum time required to paint all boards under the constraints that any painter will only paint contiguous sections of board % 10000003.

Example Input:
Input 1:
A = 2
B = 5
C = [1, 10]

Input 2:
A = 10
B = 1
C = [1, 8, 11, 3]

Example Output:
Output 1: 50
Output 2: 11

Example Explanation:
Explanation 1:
Possibility 1: One painter paints both blocks, time taken = 55 units.
Possibility 2: Painter 1 paints block 1, painter 2 paints block 2, time taken = max(5, 50) = 50
There are no other distinct ways to paint boards. Answer = 50 % 10000003.

Explanation 2:
Each block is painted by a painter so, Painter 1 paints block 1, painter 2 paints block 2, painter 3 paints block 3,
and painter 4 paints block 4, time taken = max(1, 8, 11, 3) = 11. Answer = 11 % 10000003.
"""

class Solution:
    # Initializes the Solution with parameters for painters, time per unit, and board lengths
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def paint(self):
        # Multiply each board length by the time per unit to get the painting times
        for i in range(len(self.C)):
            self.C[i] = self.C[i] * self.B

        # Set the search range for binary search
        l = max(self.C)  # Minimum possible time
        r = sum(self.C)  # Maximum possible time

        ans = 0
        while l <= r:
            mid = l + (r - l) // 2
            if self.check(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans % 10000003

    def check(self, mid):
        no_of_painters = 1
        cur_work = 0
        for i in range(len(self.C)):
            if cur_work + self.C[i] <= mid:
                cur_work += self.C[i]
            else:
                no_of_painters += 1
                cur_work = self.C[i]
                if no_of_painters > self.A:
                    return False
        return True

def main():
    # Example inputs
    A1, B1, C1 = 2, 5, [1, 10]  # Expected output: 50
    A2, B2, C2 = 10, 1, [1, 8, 11, 3]  # Expected output: 11

    # Create solution instances for each example input
    solution1 = Solution(A1, B1, C1)
    solution2 = Solution(A2, B2, C2)

    # Print the results
    print(f"Minimum time required for example 1: {solution1.paint()}")
    print(f"Minimum time required for example 2: {solution2.paint()}")

if __name__ == "__main__":
    main()
