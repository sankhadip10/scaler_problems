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