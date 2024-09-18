# Author: Claudia Sitiriche
# Github Username: sitiricc
# Date: February 22, 2023
# Description: Project 7- This project has a linked list that has recursive
# implementations and adds, removes and reverses from list.


class Node:
    """
    Represents a node in a linked list.
    """
    def __init__ (self, data):
        self.data= data                         # holds value we're storing in the Node
        self.next= None                         # Next node in list. Initializes to None because there are no nodes in the list yet.


class LinkedList:
    """
    A linked list implementation of the List ADT
    """
    def __init__(self):
        self._head= None                        # Used to keep track of the first node in the list

    def get_head(self):
        """
        Get method for head
        """
        return self._head

    def rec_add(self, current, val):
        """
        Recursive method that adds a node containing val to the end of the linked list.
        """
        if current.next is None:              # If next node is empty
            current.next = Node(val)          # adds next on the list if node not in list
            return                            # return current node
        self.rec_add(current.next, val)       # recursion for add method

    def add(self, val):
        """
        Helper method user will call the recursive function and passes the value to be added.
        """
        if self._head is None:                # if node is empty
            self._head= Node(val)             # add node
        else:
            self.rec_add(self._head, val)     # recursion for add method

    def rec_display(self, a_node):
        """recursive display method"""
        if a_node is None:                   # if the value a_node is empty
            return
        print(a_node.data, end=" ")          # print to screen
        self.rec_display(a_node.next)        # recursion for display method

    def display(self):
        """recursive display helper method"""
        self.rec_display(self._head)        # recursion for display method

    def rec_remove(self, current, val):
        """
        Recursive method that removes from the list a node containing val.
        """
        if current is None:                     # checks to see if the list is empty. If so, simply returns.
            return
        if current.data == val:                 # checks to see if head should be removed.
            return current.next                 # if head should be removed, then it makes head refer to the next Node.
        current.next= self.rec_remove(current.next, val)    # recursion for rec_remove
        return current

    def remove (self, val):
        """
        Helper method user will call the recursive function and passes the value to be removed.
        """
        self._head= self.rec_remove(self._head, val)                          # calls recursive function

    def rec_contains(self, key):
        """
        Recursive method that returns True if the list contains a Node with the value key,
        otherwise returns False
        """
        if self._head is None:              # If the list is empty
            return False                    # returns false
        if self._head is not None:          # if list is not None
            if self._head.data == key:      # if list contains a Node with value key
                return True                 # return True
            self._head = self._head.next    # For next node

    def contains(self, val):
        """
        Helper method for recursive contains method.
        """
        self.rec_contains(self._head, val)         #helper for recursive contains method.

    def rec_insert(self, val, pos):
        """
         Inserts a node containing val into the linked list at position pos
         """
        if self._head is None:                          # If the list is empty
            self.add(val)
            return
        if pos == 0:
            temp = self._head
            self._head = Node(val)
            self._head.next = temp
        else:
            current = self._head
            for _ in range(pos-1):
                if current.next is None:
                    current.next = Node(val)
                    return
                current = current.next
            temp = current.next
            current.next = Node(val)
            current.next.next = temp

    def insert(self, val):
        """Helper method for rec_insert function."""
        self.rec_insert(self._head, val)

    def rec_reverse(self):
        """"
        Recursive method that reverses the linked list.
        """
        previous = None
        current= self._head
        if current is not None:
            following = current.next
            current.next = previous
            previous = current
            current = following
        self._head = previous

    def reverse(self):
        """Helper method for reverse."""
        self.rec_reverse(self._head)

    def rec_to_plain_list(self):
        """
        Returns a regular Python list containing the same values,
        in the same order, as the linked list
        """
        result = []                         # empty list
        current = self._head
        if current is not None:             # if Node not empty
            result += [current.data]        # add to data
        return result                       # return list

    def to_plain_list(self):
        """Helper method for reverse."""
        self.rec_remove(self._head)


def main():
    mylist = LinkedList()
    mylist.add(8)
    mylist.add(9)
    mylist.remove(9)
    mylist.add(10)
    mylist.add(11)


    mylist.reverse()
    mylist.display()



if __name__ == '__main__':
    main()
