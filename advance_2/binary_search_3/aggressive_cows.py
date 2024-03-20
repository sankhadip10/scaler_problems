# def generate_combinations(arr, start, end, index, r, combinations):
#     """
#     A utility function to generate combinations of r elements in the given array.
#     """
#     # Current combination is ready to be added
#     if index == r:
#         combinations.append(arr[:r])
#         return
#
#     # When no more elements are there to put in the array
#     if start >= end:
#         return
#
#     # Current is included, put next at next location
#     arr[index] = start
#     generate_combinations(arr, start + 1, end, index + 1, r, combinations)
#
#     # Current is excluded, replace it with next (Note that i+1 is passed, but index is not changed)
#     generate_combinations(arr, start + 1, end, index, r, combinations)
#
#
# def min_distance(stalls, combination):
#     """
#     Calculate the minimum distance between any two cows in the given combination of stalls.
#     """
#     min_dist = float('inf')
#     for i in range(1, len(combination)):
#         min_dist = min(min_dist, stalls[combination[i]] - stalls[combination[i - 1]])
#     return min_dist
#
#
# def brute_force_aggressive_cows(stalls, B):
#     """
#     Find the largest minimum distance possible among the cows using brute force.
#     """
#     N = len(stalls)
#     stalls.sort()  # Sort the stalls for easier distance calculation
#     combinations = []
#     arr = [0] * B
#     generate_combinations(arr, 0, N, 0, B, combinations)
#
#     max_min_dist = 0
#     for combination in combinations:
#         curr_min_dist = min_distance(stalls, combination)
#         max_min_dist = max(max_min_dist, curr_min_dist)
#
#     return max_min_dist
#
#
# # Example usage
# stalls = [1, 2, 3, 4, 5]
# B = 3
# print(brute_force_aggressive_cows(stalls, B))
#
# stalls = [1, 2]
# B = 2
# print(brute_force_aggressive_cows(stalls, B))
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        n = len(A)
        l = 1
        r = A[n - 1] - A[0]
        ans = 0
        while (l <= r):
            mid = l + (r - l) // 2

            if self.check(A, mid, B):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

    def check(self, A, mid, B):
        n = len(A)
        last_placed_cow = A[0]
        num_of_cow_placed = 1
        for i in range(1, n):
            if A[i] - last_placed_cow >= mid:
                last_placed_cow = A[i]
                num_of_cow_placed += 1

            if num_of_cow_placed >= B:
                return True
        return False


def main():
    # Example usage
    solution = Solution()
    # Example stall positions
    stalls = [1, 2, 4, 8, 9]
    # Number of cows
    cows = 3
    # Solve for the maximum minimum distance
    max_min_distance = solution.solve(stalls, cows)
    print(f"Maximum minimum distance: {max_min_distance}")


if __name__ == "__main__":
    main()
