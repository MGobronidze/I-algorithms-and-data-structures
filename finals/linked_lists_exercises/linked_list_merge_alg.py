# Java Program to merge two sorted linked list using
# recursion

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

# Takes two lists sorted in increasing order, and splices
# their nodes together to make one big sorted list which is
# returned
def merge_sorted_list(a, b):
    result = None

    # Base cases
    if a is None:
        return b
    elif b is None:
        return a

    # Pick either a or b, and recur
    if a.data <= b.data:
        result = a
        result.next = merge_sorted_list(a.next, b)
    else:
        result = b
        result.next = merge_sorted_list(a, b.next)
    return result


# Create a hard-coded linked list:
# 2 -> 4 -> 8 -> 9
a = Node(2)
a.next = Node(4)
a.next.next = Node(8)
a.next.next.next = Node(9)

# Create another hard-coded linked list:
# 1 -> 3 -> 8 -> 10
b = Node(1)
b.next = Node(3)
b.next.next = Node(8)
b.next.next.next = Node(10)

merged_list = merge_sorted_list(a, b)

temp = merged_list
print("Merged Sorted Linked List is:")
while temp:
        print(temp.data, end=" ")
        temp = temp.next