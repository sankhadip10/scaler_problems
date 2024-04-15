# Problem Description:
# Design and implement a Linked List data structure.
# A node in a linked list should have the following attributes - an integer value and a pointer to the next node.
#
# It should support the following operations:
# - insert_node(position, value): To insert the input value at the given position in the linked list.
# - delete_node(position): Delete the value at the given position from the linked list.
# - print_ll(): Print the entire linked list, such that each element is followed by a single space (no trailing spaces).
#
# Note:
# - If an input position does not satisfy the constraint, no action is required.
# - Each print query has to be executed in a new line.
#
# Problem Constraints:
# - 1 <= value <= 10^5
# - 1 <= position <= n where n is the size of the linked list.
#
# Input Format:
# - The first line contains an integer denoting the number of cases, let's say t.
# - The next t lines denote the cases.
#
# Output Format:
# - When there is a case of print_ll(), Print the entire linked list, such that each element is followed by a single space.
# - There should not be any trailing space.
#
# Example Input:
# Input 1:
# 5
# i 1 23
# i 2 24
# p
# d 1
# p
# Input 2:
# 3
# i 1 54
# d 10
# p
#
# Example Output:
# Output 1:
# 23 24
# 24
# Output 2:
# 54
#
# Example Explanation:
# Explanation 1:
# After the first two cases, the linked list contains two elements: 23 and 24.
# At the third case, print: 23 24.
# At the fourth case, delete the value at the first position, leaving only one element, 24.
# At the fifth case, print: 24.
# Explanation 2:
# After the first case, the linked list contains: 54
# At the second case, delete the value at the 10th position. Since the position is higher than the length of the linked list, it does not satisfy the constraint, so no action is required.
# At the third case, print: 54.
class Node:
    def __init__(self, x):
        self.value = x
        self.next = None


head = None
size_of_ll = 0


def insert_node(position, value):
    global head
    global size_of_ll

    if position >= 1 and position <= size_of_ll + 1:
        temp = Node(value)
        if position == 1:
            temp.next = head
            head = temp
        else:
            count = 1
            prev = head
            while count < position - 1 and prev.next is not None:
                prev = prev.next
                count += 1

            temp.next = prev.next
            prev.next = temp

        size_of_ll += 1


def delete_node(position):
    global head
    global size_of_ll

    if position >= 1 and position <= size_of_ll + 1:
        temp = None
        if position == 1:
            temp = head
            head = head.next
        else:
            count = 1
            prev = head
            while count < position - 1 and prev.next is not None:
                prev = prev.next
                count += 1

            if prev.next is not None:
                temp = prev.next
                prev.next = prev.next.next

        size_of_ll -= 1


def print_ll():
    global head
    global size_of_ll

    temp = head
    ans = []
    while temp is not None:
        ans.append(str(temp.value))
        temp = temp.next

    print(" ".join(ans))


def main():
    global head
    global size_of_ll

    cases = int(input("Enter the number of cases: "))
    for _ in range(cases):
        inputs = input().split()
        if inputs[0] == 'i':
            position = int(inputs[1])
            value = int(inputs[2])
            insert_node(position, value)
        elif inputs[0] == 'd':
            position = int(inputs[1])
            delete_node(position)
        elif inputs[0] == 'p':
            print_ll()


if __name__ == "__main__":
    main()
