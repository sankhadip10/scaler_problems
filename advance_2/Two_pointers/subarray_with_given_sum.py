"""
Problem Description:
Given an array of positive integers A and an integer B, find and return the first continuous subarray which adds to B.
If the answer does not exist, return an array with a single integer "-1".
First sub-array means the sub-array for which the starting index is minimum.

Problem Constraints:
1 <= length of the array <= 100000
1 <= A[i] <= 10^9
1 <= B <= 10^9

Input Format:
The first argument given is the integer array A.
The second argument given is integer B.

Output Format:
Return the first continuous sub-array which adds to B and if the answer does not exist return an array with a single integer "-1".

Example Input:
Input 1: A = [1, 2, 3, 4, 5], B = 5
Input 2: A = [5, 10, 20, 100, 105], B = 110

Example Output:
Output 1: [2, 3]
Output 2: [-1]

Example Explanation:
Explanation 1: [2, 3] sums up to 5.
Explanation 2: No subarray sums up to the required number.
"""
# =======================================================================================================
# def get_all_subarrays(arr):
#     subarrays = []  # This will store all subarrays
#     n = len(arr)
#
#     # Outer loop picks the starting point
#     for start in range(n):
#         # Middle loop picks the ending point
#         print("       ")
#         for end in range(start, n):
#             # Inner loop adds the subarray
#             subarray = arr[start:end + 1]
#             subarrays.append(subarray)
#             print(subarrays)
#
#     return subarrays

# _______________________________________________________________________________________________________
# def find_subarray_brute_force(A, B):
#     n = len(A)
#     for i in range(n):
#         current_sum = 0
#         for j in range(i, n):
#             current_sum += A[j]
#             if current_sum == B:
#                 return A[i:j+1]
#     return [-1]
#
# # Example usage
# arr = [1, 2, 3,4,5]
# B = 9
# subarrays = find_subarray_brute_force(arr,B)
# print(subarrays)
# print("All subarrays:")
# for subarray in subarrays:
#     print(subarray)
# TC---o(n2)
# SC---o(1)
# ________________________________________________________________________________________________________
# def find_subarray_optimized(A,B):
#     cum_sum = 0
#     hm = {0:-1}
#     for i, num in enumerate(A):
#         cum_sum += num
#         print(hm)
#         if cum_sum-B in hm:
#             return A[hm[cum_sum - B] + 1:i+1]
#         hm[cum_sum] = i
#     return[-1]
#
# A = [1,2,3,4,5]
# B =5
# result=find_subarray_optimized(A,B)
# print(result)
# ---------------------------------------------------------------------------------------------------------
def find_subarray_two_pointers(A, B):
    left, right = 0, 0
    current_sum = A[0]
    while left < len(A) and right < len(A):
        if current_sum == B:
            return A[left:right + 1]
        if current_sum < B and right < len(A) - 1:
            right += 1
            current_sum += A[right]
        else:
            current_sum -= A[left]
            left += 1
            if left > right and left < len(A):
                right = left
                current_sum = A[left]
    return [-1]


def main():
    # Example input arrays and target sum B
    examples = [([1, 2, 3, 4, 5], 5), ([5, 10, 20, 100, 105], 110)]

    for A, B in examples:
        result = find_subarray_two_pointers(A, B)
        print(f"Array: {A}, Target Sum: {B} => First Subarray: {result}")


if __name__ == "__main__":
    main()
