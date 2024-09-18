# Author: Todd Goldfarb
# GitHub username: ToddGoldfarb-OSU
# Date: 2/21/2023
# Description: The LinkedList Class with all of the corresponding recursive methods
# of a traditional Linked List class.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Initialization method."""
    def __init__(self):
        self._head = None

    def get_head(self):
        return self._head

    def add(self, value, current_node=None):
        if self._head is None:
            """We haven't started the LinkedList, so start it."""
            self._head = Node(value)
            return
        else:
            """We can assume that we can move on, we have a head."""
            """We need to define currentNode"""
            if current_node is None:
                current_node = self._head
            if current_node.next is None:
                """The node in front is empty, so that is where our new value 
goes."""
                current_node.next = Node(value)
                return
            else:
                """There is a node in front of our current node, therefore we 
recurse one step further."""
                self.add(value, current_node.next)

    def to_plain_list(self, current_node=None, list=None):
        """recursive display method"""
        if list is None:
            """Create List and initialize, also handle empty node case"""
            list = []
            if self._head is not None:
                list.append(self._head.data)
                return self.to_plain_list(self._head.next, list)
            else:
                return list
        if current_node is None:
            """Assume we are at end of list."""
            return list
        """Not at end of list, have a head, and current_node is not empty."""
        list.append(current_node.data)
        return self.to_plain_list(current_node.next, list)

    def to_regular_list(self, current_node=None, list=None):
        """recursive LIST METHOD, USED AS HELPER FOR REVERSE"""
        """INSTEAD OF JUST CREATING A LIST OF DATAS, IT CREATES ALIST OF NODES"""
        if list is None:
            """Create List and initialize, also handle empty node case"""
            list = []
            if self._head is not None:
                list.append(self._head)
                return self.to_regular_list(self._head.next, list)
            else:
                return list
        if current_node is None:
            """Assume we are at end of list."""
            return list
        """Not at end of list, have a head, and current_node is not empty."""
        list.append(current_node)
        return self.to_regular_list(current_node.next, list)

    def remove(self, value, current_node=None, previous_node=None):
        """recursive remove value from list"""
        """ ALL EDGE CASES """
        if self._head is None:
            """There is nothing in the linked list"""
            return
        if self._head.data == value:
            self._head = self._head.next
            return
        "travel until current_node is the value we want"
        """We might be at the beginning"""
        if current_node is None:
            current_node = self._head
            if current_node.next is None:
                """We failed to find the value"""
                return
            return self.remove(value, current_node.next, current_node)
        """Then we simply link previous_node.next = current_node.next"""
        if current_node.data == value:
            previous_node.next = current_node.next
        else:
            if current_node.next is None:
                """We failed to find the value"""
                return
            self.remove(value, current_node.next, current_node)

    def contains(self, value, current_node=None):
        """returns true or false if value is in linked list"""
        if current_node is None:
            current_node = self._head
        if current_node.data == value:
            return True
        else:
            if current_node.next is None:
                return False
            return self.contains(value, current_node.next)

    def insert(self, value, desiredPosition, current_node=None,previous_node=None, counter=None):
        """inserts node at desired position with desired value, starting at 0"""
        """EDGE CASE"""
        if desiredPosition == 0:
            tempHolder = self._head
            self._head = Node(value)
            self._head.next = tempHolder
            return
        """RECURSE UNTIL FIND POSITION"""
        if counter is None:
            counter = 0
            current_node = self._head
        if desiredPosition == counter:
            previous_node.next = Node(value)
            previous_node.next.next = current_node
        else:
            self.insert(value, desiredPosition, current_node.next, current_node, counter+1)

    def reverse(self, reference_list=None, counter=None, current_node=None):
        """recursively reverse list"""
        if reference_list is None:
            reference_list = self.to_regular_list()
            counter = len(reference_list) - 1
            self._head = reference_list[counter]
            self.reverse(reference_list, counter-1, self._head)
            return
        """Now we can start at the final position and move backwards"""
        """Take current_node, it's next is what is next in the reference list and move on"""
        if counter < 0:
            """We have reached the end of reference_list"""
            return
        current_node.next = reference_list[counter]
        self.reverse(reference_list, counter-1, reference_list[counter])

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