# Given the price list at which tickets for a flight were purchased,
# figure out the kth smallest price for the flight.
# kth smallest price is the minimum possible n such that there are at least k price elements in the price
# list with value <= n.
# In other words, if the price list was sorted, then A[k-1] (k is 1 based, while the array is 0 based).
#
# NOTE: You are not allowed to modify the price list (The price list is read-only).
# Try to do it using constant extra space.
#
# Example:
#
# A : [2, 1, 4, 3, 2]
# k : 3
#
# Answer : 2
# Constraints:
#
# 1 <= number of elements in the price list <= 1000000
# 1 <= k <= number of elements in the price list
# The solution should find the kth smallest price using binary search to maintain constant space
# complexity.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# def find_kth_smallest(nums, k):
#     # Sort the array
#     sorted_nums = sorted(nums)
#
#     # Return the kth smallest element
#     # Note: k is 1-based, Python lists are 0-based
#     return sorted_nums[k - 1]
#
#
# # Example usage
# nums = [6, 1, 4, 7, 8]
# k = 4
# print(find_kth_smallest(nums, k))

# time complexity - o(nlogn)
# space complexity - o(n)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        l = min(A)
        r = max(A)
        ans = 0
        while (l <= r):
            mid = l + (r - l) // 2
            if self.check(A, mid, B):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

    def check(self, A, mid, k):
        ans = sum(1 for i in A if i < mid)

        return ans < k

# t.c-nlog(max-min)
# s.c - o(1)

def main():
    # Create an instance of the Solution class
    sol = Solution()

    # Define the price list and the value of k
    prices = (2, 1, 4, 3, 2)  # Example price list as a tuple
    k = 3  # Example value of k

    # Call the solve method with the prices and k
    kth_smallest_price = sol.solve(prices, k)

    # Print the kth smallest price
    print(f"The {k}th smallest price is: {kth_smallest_price}")

if __name__ == "__main__":
    main()

