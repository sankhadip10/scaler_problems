# Reverse a linked list A from position B to C.
#
# NOTE: Do it in-place and in one-pass.
#
#
# Problem Constraints
# 1 <= |A| <= 106
#
# 1 <= B <= C <= |A|
#
#
# Input Format
# The first argument contains a pointer to the head of the given linked list, A.
#
# The second arugment contains an integer, B.
#
# The third argument contains an integer C.
#
#
# Output Format
# Return a pointer to the head of the modified linked list.
#
#
# Example Input
# Input 1:
#  A = 1 -> 2 -> 3 -> 4 -> 5
#  B = 2
#  C = 4
#
# Input 2:
#  A = 1 -> 2 -> 3 -> 4 -> 5
#  B = 1
#  C = 5
#
#
# Example Output
# Output 1:
#  1 -> 4 -> 3 -> 2 -> 5
# Output 2:
#  5 -> 4 -> 3 -> 2 -> 1
#
#
# Example Explanation
# Explanation 1:
#
#  In the first example, we want to reverse the highlighted part of the given linked list : 1 -> 2 -> 3 -> 4 -> 5
#  Thus, the output is 1 -> 4 -> 3 -> 2 -> 5
# Explanation 2:
#
#  In the second example, we want to reverse the highlighted part of the given linked list : 1 -> 4 -> 3 -> 2 -> 5
#  Thus, the output is 5 -> 4 -> 3 -> 2 -> 1

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse(self, head, B, C):
        prev = None
        curr = head

        if head and B <= C:
            while B <= C:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                B += 1
        if head:
            head.next = curr
        return prev

    def reverseBetween(self, A, B, C):
        curr = A
        prev = None
        count = 1
        while count < B:
            prev = curr
            curr = curr.next
            count += 1
        if prev:
            prev.next = self.reverse(curr, B, C)
        return A

def printLinkedList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

if __name__ == "__main__":
    # Create a linked list
    A = ListNode(1)
    A.next = ListNode(2)
    A.next.next = ListNode(3)
    A.next.next.next = ListNode(4)
    A.next.next.next.next = ListNode(5)

    # Create an instance of the Solution class
    sol = Solution()

    # Reverse the sublist from position B to C
    B = 2
    C = 4
    result = sol.reverseBetween(A, B, C)

    # Print the modified linked list
    printLinkedList(result)

# t.c-o(n)
# s.c-o(1)