# Problem Description
# Given a matrix A of size Nx3 representing operations. Your task is to design the linked list based on these operations.
#
# There are four types of operations:
#
# 0 x -1: Add a node of value x before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# 1 x -1: Append a node of value x to the last element of the linked list.
# 2 x index: Add a node of value x before the indexth node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
# 3 index -1: Delete the indexth node in the linked list, if the index is valid.
# A[i][0] represents the type of operation.
#
# A[i][1], A[i][2] represents the corresponding elements with respect to type of operation.
#
# Note: Indexing is 0 based.
#
#
# Problem Constraints
# 1 <= Number of operations <= 1000
# 1 <= All node values <= 109
#
#
# Input Format
# The only argument given is matrix A.
#
#
# Output Format
# Return the pointer to the starting of the linked list.
#
#
# Example Input
# Input 1:
#     A = [   [0, 1, -1]
#             [1, 2, -1]
#             [2, 3, 1]   ]
# Input 2:
#     A = [   [0, 1, -1]
#             [1, 2, -1]
#             [2, 3, 1]
#             [0, 4, -1]
#             [3, 1, -1]
#             [3, 2, -1]  ]
#
#
# Example Output
# Output 1:
#     1->3->2->NULL
#
# Output 2:
#     4->3->NULL
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.head = None
        self.size = 0

    def solve(self, A):
        for item in A:
            if item[0] == 0:
                self.addAtFirst(item[1])
            elif item[0] == 1:
                self.addAtLast(item[1])
            elif item[0] == 2:
                self.addNode(item[1], item[2])
            elif item[0] == 3:
                self.delete(item[1])

        return self.head

    def addAtFirst(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            new_node = ListNode(value)
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def addAtLast(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            new_node = ListNode(value)
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
        self.size += 1

    def addAtIndex(self, value, index):
        temp = self.head
        count = 0
        new_node = ListNode(value)
        while count < index - 1:
            temp = temp.next
            count += 1
        new_node.next = temp.next
        temp.next = new_node
        self.size += 1

    def addNode(self, value, index):
        if index == self.size:
            self.addAtLast(value)
        elif index > self.size or index < 0:
            return
        elif index == 0:
            self.addAtFirst(value)
        else:
            self.addAtIndex(value, index)

    def delete(self, position):
        temp = self.head
        if not self.head:
            return
        if position < self.size:
            if position == 0:
                self.head = self.head.next
            else:
                for k in range(position - 1):
                    temp = temp.next
                temp.next = temp.next.next
            self.size -= 1


# Example usage:
A1 = [
    [0, 1, -1],
    [1, 2, -1],
    [2, 3, 1]
]

A2 = [
    [0, 1, -1],
    [1, 2, -1],
    [2, 3, 1],
    [0, 4, -1],
    [3, 1, -1],
    [3, 2, -1]
]

solution = Solution()
head1 = solution.solve(A1)
head2 = solution.solve(A2)

# You can use the head nodes (head1 and head2) for further processing or display.
# Traversing and displaying the linked list with head1
print("Linked list with head1:")
current_node = head1
while current_node:
    print(current_node.val, end="->")
    current_node = current_node.next
print("NULL")

# Traversing and displaying the linked list with head2
print("Linked list with head2:")
current_node = head2
while current_node:
    print(current_node.val, end="->")
    current_node = current_node.next
print("NULL")
