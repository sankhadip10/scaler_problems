# Problem Description
# Given a linked list of integers, find and return the middle element of the linked list.
#
# NOTE: If there are N nodes in the linked list and N is even then return the (N/2 + 1)th element.
#
#
# Problem Constraints
# 1 <= length of the linked list <= 100000
#
# 1 <= Node value <= 109
#
#
# Input Format
# The only argument given head pointer of linked list.
#
#
# Output Format
# Return the middle element of the linked list.
#
#
# Example Input
# Input 1:
#
#  1 -> 2 -> 3 -> 4 -> 5
# Input 2:
#
#  1 -> 5 -> 6 -> 2 -> 3 -> 4
#
#
# Example Output
# Output 1:
#
#  3
# Output 2:
#
#  2
#
#
# Example Explanation
# Explanation 1:
#
#  The middle element is 3.
# Explanation 2:
#
#  The middle element in even length linked list of length N is ((N/2) + 1)th element which is 2.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
#
# class Solution:
#     # @param A : head node of linked list
#     # @return an integer
#     def solve(self, A):
#         head = A
#         temp = head
#         count = 1
#         mid = 0
#         while (temp.next is not None):
#             temp = temp.next
#             count += 1
#
#         mid = count // 2 + 1
#         temp = head
#
#         while mid > 1 and temp.next is not None:
#             temp = temp.next
#             mid -= 1
#
#         return temp.val
#
#
# def create_linked_list(arr):
#     if not arr:
#         return None
#     head = ListNode(arr[0])
#     current = head
#     for val in arr[1:]:
#         current.next = ListNode(val)
#         current = current.next
#     return head
#
#
# def main():
#     arr = [1, 2, 3, 4, 5]  # Example input list
#     # Create the linked list
#     linked_list = create_linked_list(arr)
#
#     # Create an instance of the Solution class
#     solver = Solution()
#
#     # Call the solve() method and print the result
#     result = solver.solve(linked_list)
#     print("Middle value of the linked list:", result)
#
#
# if __name__ == "__main__":
#     main()

# t.c-o(n+n//2)~~o(n)
# sc-o(1)


# --------------------------------------------------------------------------------------------
class Node:
    def __init__(self,x):
        self.val = x
        self.next = None

class solution:
    def find_middle(self,A):
        fast = A
        slow = A
        while(fast !=None and fast.next!=None):
            slow=slow.next
            fast=fast.next.next
        return slow

if __name__ =="__main__":
    #creating linked list
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    sol = solution()
    middle_node = sol.find_middle(head)
    print("Middle lement of the linked list is:",middle_node.val)