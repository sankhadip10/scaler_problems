# def max_subarray_size(arr, B):
#     n = len(arr)
#     max_k = 0
#
#     for k in range(1, n + 1):
#         window_sum = sum(arr[:k])
#         if window_sum > B:
#             break
#
#         valid = True
#         for i in range(1, n - k + 1):
#             window_sum = window_sum - arr[i - 1] + arr[i + k - 1]
#             if window_sum > B:
#                 valid = False
#                 break
#
#         if valid:
#             max_k = k
#
#     return max_k
#
#
# # Example usage:
# arr = [3, 2, 5, 4, 6, 3, 7, 2]
# B = 20
# result = max_subarray_size(arr, B)
# print("Max value of K:", result)
arr = [3, 2, 5, 4, 6, 3, 7, 2]
for k in range(1,9):
    windows_sum = sum(arr[:k])
    print(arr[:k],"-->",windows_sum)
