"""
Problem Description:
Given a linked list A, remove the B-th node from the end of the list and return its head.
For example, given linked list: 1->2->3->4->5, and B = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

NOTE: If B is greater than the size of the list, remove the first node of the list.

Try doing it using constant additional space.

Problem Constraints:
1 <= |A| <= 10^6

Input Format:
The first argument of input contains a pointer to the head of the linked list. The second argument of input contains the integer B.

Output Format:
Return the head of the linked list after deleting the B-th element from the end.

Example Input:
Input 1:
A = 1->2->3->4->5
B = 2
Input 2:
A = 1
B = 1

Example Output:
Output 1:
1->2->3->5
Output 2:

Example Explanation:
Explanation 1:
In the first example, 4 is the second last element.
Explanation 2:
In the second example, 1 is the first and the last element.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        temp = A
        count = 1

        while temp.next != None:
            temp = temp.next
            count += 1

        # If B is greater than or equal to the length, remove the head node
        if B >= count:
            return A.next

        # Find the node before the node to be removed
        prev = None
        current = A

        for _ in range(count - B):
            prev = current
            current = current.next

        # Remove the B-th node from the end
        if prev:
            prev.next = current.next

        return A


def printLinkedList(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    return ' -> '.join(result)


if __name__ == "__main__":
    # Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    current = head
    for i in range(2, 6):
        current.next = ListNode(i)
        current = current.next

    B = 2
    solution = Solution()
    modified_head = solution.removeNthFromEnd(head, B)
    print("Modified Linked List:", printLinkedList(modified_head))

# t.c-o(n)
# s.c-o(1)