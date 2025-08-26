# 1. Reverse an array in place
def reverse_array(arr):
    start, end = 0, len(arr) -1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start, end = start + 1, end -1
    return arr
    

# create a sample array
arr = [1, 2, 3, 4, 5]
# reverse the array
print(reverse_array(arr))
# access specific element
print(arr[2])
# insert a bulk of elements at the begin of array
arr = [-3 , -2, -1, 0] + arr
print(arr)
# add element at the end of array
arr = arr + [6, 7, 8, 9]
print(arr)
# remove element from array
del arr[0]
print(arr)
# reverse the array
print(reverse_array(arr))


def reverse_linked_list():
    pass

# create a node into a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# create a linked list
class LinkedList(Node):
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        