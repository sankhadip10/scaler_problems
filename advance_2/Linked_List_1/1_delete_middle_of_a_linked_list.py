"""
Given a singly linked list, delete middle of the linked list.

For example, if given linked list is 1->2->3->4->5 then linked list should be modified to 1->2->4->5

If there are even nodes, then there would be two middle nodes, we need to delete the second middle element.

For example, if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.

Return the head of the linked list after removing the middle node.

If the input linked list has 1 node, then this node should be deleted and a null node should be returned.


Input Format

The only argument given is the node pointing to the head node of the linked list
"""
# Brute Force
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# class Solution:
#     def find_middle(self, A):
#         head = A
#         temp = A
#         count = 0
#         while temp.next is not None:
#             count += 1
#             temp = temp.next
#         middle = count // 2
#         temp = head
#         while temp is not None:
#             middle -= 1
#             if middle == 0:
#                 temp.next = temp.next.next
#                 break
#             temp = temp.next
#         return head
#
# def printLinkedList(head):
#     current = head
#     while current:
#         print(current.val, end=" -> ")
#         current = current.next
#     print("None")
#
# def main():
#     # Create a linked list
#     head = ListNode(1)
#     head.next = ListNode(2)
#     head.next.next = ListNode(3)
#     head.next.next.next = ListNode(4)
#     head.next.next.next.next = ListNode(5)
#
#     # Print original linked list
#     print("Original Linked List:")
#     printLinkedList(head)
#
#     # Create an instance of the Solution class
#     solution = Solution()
#
#     # Call the find_middle method
#     new_head = solution.find_middle(head)
#
#     # Print modified linked list
#     print("\nLinked List after removing middle node:")
#     printLinkedList(new_head)
#
# if __name__ == "__main__":
#     main()

# t,c~~o(n+n/2)
# s.c-0(1)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def solve(self, A):
        head = A
        if head == None or head.next == None:
            return None

        slow = A
        fast = A
        fast = A.next.next

        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return head


def printLinkedList(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


def main():
    # Create a linked list
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # Print original linked list
    print("Original Linked List:")
    printLinkedList(head)

    # Create an instance of the Solution class
    solution = Solution()

    # Call the solve method
    new_head = solution.solve(head)

    # Print modified linked list
    print("\nLinked List after removal:")
    printLinkedList(new_head)


if __name__ == "__main__":
    main()


# time complexit~~o(n/2)
# space complexity~~O(1)