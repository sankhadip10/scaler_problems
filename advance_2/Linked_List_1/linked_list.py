# Problem Description
# * Task: Build a custom Linked List data structure.
# * Node Structure:
#     * value: An integer to store data.
#     * pointer: A reference to the subsequent node in the list.

# Supported Operations
# * insert_node(position, value):
#     * Inserts a new node with the specified `value` at a given `position` within the list.
# * delete_node(position):
#     * Removes the node located at the provided `position`.
# * print_ll():
#     * Displays all elements in the Linked List, with each element separated by a single space.

# Constraints
# * Value Range: 1 <= `value` <= 105
# * Position Range: 1 <= `position` <= `n` (where `n` is the current Linked List size)
# * Invalid Input: Operations with out-of-bounds positions are ignored.

# Input/Output
# * Input:
#     * The first line is a number indicating test cases.
#     * Subsequent lines are commands:
#         * 'i' for insert
#         * 'd' for delete
#         * 'p' for print
# * Output:
#     * Each 'print_ll' command produces a line of space-separated list elements.

# Example Input / Output (Refer to the original problem text for detailed examples)

# ****  Your Linked List Implementation Would Go Below ****

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class LinkedList:  # Introduce a class for better organization
    def __init__(self):
        self.head = None
        self.size_of_ll = 0

    def insert(self, position, value):
        if 1 <= position <= self.size_of_ll + 1:  # Allow insertion at the end
            x = Node(value)
            if position == 1:
                x.next = self.head
                self.head = x
            else:
                temp = self.head
                count = 1
                while count < position - 1:
                    temp = temp.next
                    count += 1
                x.next = temp.next
                temp.next = x
            self.size_of_ll += 1

    def delete(self, position):
        if 1 <= position <= self.size_of_ll:
            if position == 1:
                self.head = self.head.next
            else:
                count = 1
                temp = self.head
                while count < position - 1:
                    temp = temp.next
                    count += 1
                temp.next = temp.next.next
            self.size_of_ll -= 1

    def print(self):  # Renamed from 'print' for clarity
        temp = self.head
        ans = []
        while temp is not None:
            ans.append(str(temp.val))
            temp = temp.next
        print(" ".join(ans))


# ... (Your Node and LinkedList class definitions from before)

def main():
    num_test_cases = int(input())  # Read the number of test cases

    for _ in range(num_test_cases):
        linked_list = LinkedList()  # Create a Linked List for each test case
        commands = input().split()  # Get commands

        for cmd in commands:
            if cmd == 'i':
                position, value = map(int, input().split())
                linked_list.insert(position, value)
            elif cmd == 'd':
                position = int(input())
                linked_list.delete(position)
            elif cmd == 'p':
                linked_list.print()


if __name__ == "__main__":
    main()
