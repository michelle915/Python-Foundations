# Author: Christopher Partin
# GitHub username: Korachof
# Date: 2/20/2023
# Description: A program that creates a linked list of numbers using an add function. It can remove numbers, check
#   to see which numbers are contained in the list, insert numbers at specific positions in the list, reverse the list,
#   and create a normal python list using the numbers within. Everything is recursive.


class Node:
    """Node class for LinkedList"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """A class that creates a Linked List of numbers """

    def __init__(self):
        self._head = None

    def add(self, value):
        """Helper function for add_recursion"""
        return self.add_recursion(value, self._head)

    def add_recursion(self, value, head):
        """Adds a node containing value to end of the LinkedList"""
        if head is None:  # if the list is empty, add to head.
            self._head = Node(value)
        else:
            current = head
            if current.next is not None:
                current = current.next
                return self.add_recursion(value, current)
            current.next = Node(value)

    def remove(self, value):
        """Helper function for remove_recursion"""
        return self.remove_recursion(value, self._head, previous=None)

    def remove_recursion(self, value, current, previous):
        """Recursive function that removes a specific element from the Linked
List"""
        if self._head is None:
            return
        if self._head.data == value:
            self._head = self._head.next
        else:
            if current is not None and current.data != value:
                previous = current
                current = current.next
                return self.remove_recursion(value, current, previous)
            if current is not None:  # we found the correct one!
                previous.next = current.next

    def contains(self, value):
        """Helper function for contains_recursion"""
        return self.contains_recursion(value, self._head, previous=None)

    def contains_recursion(self, value, current, previous):
        """Returns True if the element is in the Linked List object, False
otherwise"""
        if self._head is None:
            return False
        if self._head.data == value:
            return True
        else:
            if current is not None and current.data != value:
                previous = current
                current = current.next
                return self.contains_recursion(value, current, previous)
            if current is not None:
                return True
            if current is None:
                return False

    def insert(self, value, position):
        """Helper function for insert_recursion"""
        return self.insert_recursion(value, position, self._head, counter=0)

    def insert_recursion(self, value, position, current, counter):
        """Inserts an element at the specified position in the Linked List"""
        if self._head is None:
            self._head = Node(value)
        if position - 1 == counter:
            reconnect = current.next
            current.next = Node(value)
            current.next.next = reconnect
        else:
            counter += 1
            if current.next is not None:
                current = current.next
                return self.insert_recursion(value, position, current, counter)

    def reverse(self):
        """Helper function for reverse_recursion"""
        return self.reverse_recursion(self._head, previous=None)

    def reverse_recursion(self, current, previous):
        """Recursive function that reverses the entire Linked List by changing the
link between the nodes"""
        if self._head is None:
            return
        if previous is None:
            new_current = previous
            previous = current.next
            current.next = new_current
            return self.reverse_recursion(current, previous)
        if previous is not None:
            new_current = current
            current = previous
            previous = current.next
            current.next = new_current
            if previous is None:
                self._head = current
                return
            return self.reverse_recursion(current, previous)

    def to_plain_list(self, plain_list=None, current=None):
        """Recursive function that turns the Linked List object into a regular
Python list"""
        if plain_list is None:
            plain_list = []
        if current is None:
            current = self._head
        if self._head is None:
            return plain_list
        else:
            plain_list.append(current.data)
            if current.next is None:
                return plain_list
            current = current.next
            return self.to_plain_list(plain_list, current)

    def get_head(self):
        """Get the head of the Linked List"""
        return self._head

    def display(self):
        """
        Prints out the values in the linked list
        """
        current = self._head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

def main():
    mylist = LinkedList()
    mylist.add(8)
    mylist.add(9)
    mylist.add(10)
    mylist.add(11)
    mylist.insert(7, 5)
    mylist.display()


if __name__ == '__main__':
    main()
