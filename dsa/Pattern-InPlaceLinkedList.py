"""
1. Problem : Reverse a Singly Linked List 
> Given the head of a Singly LinkedList, reverse the LinkedList. Write a function to return the new head of the reversed LinkedList.
 
2. Problem : SubListReversal from position p and q
> Given the head of a LinkedList and two positions p and q, reverse the LinkedList from position p to q.
Ideal
- Iterate p-1 times to reach the start of the sub-list. 
Keep track of the node before the sub-list (last_node_of_first_part) and the first node of the sub-list (last_node_of_sub_list).
- Reverse the sub-list i.e nodes from p to q using the same approach as in Problem 1.
- Connect the reversed sub-list back to the original list carefully : 
    - Connect last_node_of_first_part.next to the new head of the reversed sub-list (previous).
    - Connect last_node_of_sub_list.next to the node that was originally after q (current).
3. Problem : Reverse every K-element Sub-list
> Given the head of a LinkedList and a number k, reverse every k-sized sub-list starting from the head. If the last sub-list has fewer than k elements, reverse it too.
Ideal : 
- 
"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def printList(self):
        current = self
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")
    # problem-1 : LinkedList Reversal
    def ReverseV1(self):
        previous = None
        current = self
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous
    # Problem-2 : Sublist Reversal from position p and q
    def ReverseV2(self, p, q):
        if p == q:
            return self

        # Skip the first p-1 nodes
        current, previous = self, None
        i = 0
        # Find the last node of the first part
        while current is not None and i < p - 1:
           previous = current # Node before the sub-list
           current = current.next # First node of the sub-list
           i += 1

        # Reverse the sub-list
        last_node_of_first_part = previous
        last_node_of_sub_list = current
        next = None
        i = 0
        while current is not None and i < q - p + 1:
            next = current.next
            current.next = previous
            previous = current
            current = next
            i += 1

        # Connect the reversed sub-list back to the original list
        if last_node_of_first_part is not None:
            last_node_of_first_part.next = previous
        else:
            head = previous
        last_node_of_sub_list.next = current

        return self
    def ReverseV3(self, k):
        if k <= 1 or self is None:
            return self

        current = self
        previous = None
        count = 0

        # Reverse the first k elements
        while current is not None and count < k:
            next = current.next
            current.next = previous
            previous = current
            current = next
            count += 1

        # Recursively reverse the remaining elements
        if current is not None:
            self.next = current.ReverseV3(k)

        return previous
     

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)   
    print("Original List:")
    head.printList()

    # problem-1 : LinkedList Reversal
    head = head.ReverseV1()
    print("Reversed List:")
    head.printList()

    # problem-2 : Sublist Reversal
    head = head.ReverseV2(1, 3)
    print("Sublist Reversed List:")
    head.printList()