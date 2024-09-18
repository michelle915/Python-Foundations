# Author: Michelle Loya
# GitHub username: michellealoya
# Date: 2/22/2023
# Description: The following program contains a LinkedList class with recursive implementations of methods

class Node:
    """
    Represents a node in a linked list
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A linked list implementation of the List ADT
    """
    def __init__(self):
        self._head = None

    def get_head(self):
        """
        Returns the first Node object in the list
        """
        return self._head

    def rec_add(self, value, a_node):
        """
        Recursive add method
        """
        if a_node.next is None:
            a_node.next = Node(value)
            return

        self.rec_add(value, a_node.next)

    def add(self, value):
        """
        Recursive add helper method
        """
        if self._head is None:
            self._head = Node(value)
        else:
            self.rec_add(value, self._head)

    def display(self):
        """
        Prints out the values in the linked list
        """
        current = self._head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def rec_remove(self, value, previous, current):
        """
        Recursive remove method
        """
        if current.data == value:
            previous.next = current.next
        elif current.next is not None:
            previous = current
            current = current.next
            self.rec_remove(value, previous, current)

    def remove(self, value):
        """
        Recursive remove helper method
        """
        if self._head is None:  # If the list is empty
            return
        elif self._head.data == value:  # If the node to remove is the head
            self._head = self._head.next
        elif self._head.next is not None:
            self.rec_remove(value, self._head, self._head.next)
        else:   # If the list only contains the head and the head is not the node to remove
            return

    def rec_contains(self, value, current):
        """
        Recursive contains method
        """
        if current.data == value:
            return True
        elif current.next is None:
            return False
        else:
            return self.rec_contains(value, current.next)

    def contains(self, value):
        """
        Recursive contains helper method
        """
        return self.rec_contains(value, self._head)

    def rec_insert(self, position, new_node, left_node, right_node):
        """
        Recursive insert method
        """
        if position == 1:
            left_node.next = new_node
            new_node.next = right_node
        elif right_node.next is None:
            self.add(new_node.data)
        else:
            self.rec_insert(position - 1, new_node, left_node.next, right_node.next)

    def insert(self, value, position):
        """
        Recursive insert helper method
        """
        new_node = Node(value)

        if position == 0:
            new_node.next = self._head
            self._head = new_node
        else:
            self.rec_insert(position, new_node, self._head, self._head.next)

    def rec_reverse(self, current):
        """
        Recursive reverse method
        """
        if current.next is None:
            current.next = self._head
            self._head = current
            return
        else:
            upcoming = current.next
            current.next = self._head
            self._head = current
            self.rec_reverse(upcoming)

    def reverse(self):
        """
        Recursive reverse helper method
        """

        if self._head is None:  # If the list is empty
            return
        elif self._head.next is None:  # If the list only contains the head
            return
        else:
            current = self._head.next
            upcoming = current.next
            self._head.next = None
            current.next = self._head
            self._head = current
            if upcoming is not None:
                self.rec_reverse(upcoming)

    def is_empty(self):
        """
        Returns True if the linked list is empty,
        returns False otherwise
        """
        return self._head is None

    def rec_to_plain_list(self, current, plain_list):
        """
        Returns a regular Python list containing the same values,
        in the same order, as the linked list
        """
        if current is None:
            return plain_list
        else:
            plain_list += [current.data]
            return self.rec_to_plain_list(current.next, plain_list)

    def to_plain_list(self):
        """
        Recursive to_plain_list helper method
        """
        plain_list = []
        return self.rec_to_plain_list(self._head, plain_list)


def main():
    mylist = LinkedList()
    mylist.add(8)
    mylist.add(9)
    mylist.add(10)
    mylist.add(11)
    mylist.insert(7, 0)
    mylist.reverse()
    mylist.display()
    print(mylist.to_plain_list())


if __name__ == '__main__':
    main()
