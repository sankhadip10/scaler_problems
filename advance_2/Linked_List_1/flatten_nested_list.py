# You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

# Implement the NestedIterator class:

# NestedIterator(List nestedList) Initializes the iterator with the nested list nestedList.
# int next() Returns the next integer in the nested list.
# boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.

# Example 1:
# Input: nestedList = [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,1,2,1,1].
# Example 2:
# Input: nestedList = [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,4,6].
# Constraints:
# The sum of integers in all cases does not exceed 1e5.
# The values of the integers in the nested list are in the range [-1e6, 1e6].

class NestedIterator:
    def __init__(self, nestedList):
        self.stack = []
        # Push the elements of the nestedList onto the stack in reverse order
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])


    def next(self):
        # Ensure the stack is not empty
        if self.hasNext():
            # Pop the top element from the stack
            return self.stack.pop().getInteger()

    def hasNext(self):
        # Continue until the stack is empty
        while self.stack:
            # Peek the top element from the stack
            top = self.stack[-1]
            # If it's an integer, return True
            if top.isInteger():
                return True
            # Otherwise, pop the list from the stack and flatten it
            self.stack.pop()
            for i in range(len(top.getList()) - 1, -1, -1):
                self.stack.append(top.getList()[i])
        # If the stack is empty, return False
        return False
