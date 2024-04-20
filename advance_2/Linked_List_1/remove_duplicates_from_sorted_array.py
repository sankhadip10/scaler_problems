"""
Problem Description:
Given a sorted linked list, delete all duplicates such that each element appears only once.

Problem Constraints:
0 <= length of linked list <= 10^6

Input Format:
First argument is the head pointer of the linked list.

Output Format:
Return the head pointer of the linked list after removing all duplicates.

Example Input:
Input 1:
1->1->2
Input 2:
1->1->2->3->3

Example Output:
Output 1:
1->2
Output 2:
1->2->3

Example Explanation:
Explanation 1:
Each element appears only once in 1->2.
"""


# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def deleteDuplicates(self, A):
#         head = A  # Saving the head node for return later
#         while A:  # Loop through the linked list until A is None
#             while A.next and A.next.val == A.val:  # Inner loop to check for duplicates
#                 A.next = A.next.next  # Skip duplicates by adjusting pointers
#             A = A.next  # Move to the next node
#         return head  # Return the head of the modified linked list
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
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.val, end=" -> ")
#         current = current.next
#     print("None")
#
# def main():
#     arr = [1, 1, 1, 2, 3]  # Example input
#     head = create_linked_list(arr)
#
#     solution = Solution()
#     new_head = solution.deleteDuplicates(head)
#
#     print("Original Linked List:")
#     print_linked_list(head)
#
#     print("Modified Linked List:")
#     print_linked_list(new_head)
#
# if __name__ == "__main__":
#     main()
# t.c-o(n2)
# s.c-o(1)


# ================================================

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, A):
        head = A
        current = A

        while current:
            if current.next and current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next

        return head

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

def main():
    arr = [1, 1, 1, 2, 3]  # Example input
    head = create_linked_list(arr)

    solution = Solution()
    new_head = solution.deleteDuplicates(head)

    print("Original Linked List:")
    print_linked_list(head)

    print("Modified Linked List:")
    print_linked_list(new_head)

if __name__ == "__main__":
    main()


# t.c-o(n)
# s.c-o(1)



