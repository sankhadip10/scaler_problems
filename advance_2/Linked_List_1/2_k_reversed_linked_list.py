# Problem Description
# Given a singly linked list A and an integer B, reverse the nodes of the list B at a time and return the modified linked list.
#
# Problem Constraints
# 1 <= |A| <= 10^3
# B always divides A
#
# Input Format
# The first argument of input contains a pointer to the head of the linked list.
# The second argument of input contains the integer, B.
#
# Output Format
# Return a pointer to the head of the modified linked list.
#
# Example Input
# Input 1:
# A = [1, 2, 3, 4, 5, 6]
# B = 2
# Input 2:
# A = [1, 2, 3, 4, 5, 6]
# B = 3
#
# Example Output
# Output 1:
# [2, 1, 4, 3, 6, 5]
# Output 2:
# [3, 2, 1, 6, 5, 4]
#
# Example Explanation
# Explanation 1:
# For the first example, the list can be reversed in groups of 2.
#     [[1, 2], [3, 4], [5, 6]]
# After reversing the K-linked list
#     [[2, 1], [4, 3], [6, 5]]
# Explanation 2:
# For the second example, the list can be reversed in groups of 3.
#     [[1, 2, 3], [4, 5, 6]]
# After reversing the K-linked list
#     [[3, 2, 1], [6, 5, 4]]

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, A, B):
        head = A
        curr = head
        prev = None
        count = B
        if head == None:
            return None

        while (curr != None and count > 0):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count -= 1

        new_node = self.reverseList(curr, B)
        head.next = new_node
        head = prev
        return head


def printList(head):
    curr = head
    while curr:
        print(curr.val, end=" -> ")
        curr = curr.next
    print("None")


def main():
    # Creating a sample linked list: 1 -> 2 -> 3 -> 4 -> 5 -> None
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Creating an instance of the Solution class
    solution = Solution()

    # Reversing the list in groups of size 2
    reversed_head = solution.reverseList(head, 2)

    # Printing the reversed list
    print("Reversed List:")
    printList(reversed_head)


if __name__ == "__main__":
    main()


# t.c-o(n)
# s.c-O(|A|/B)