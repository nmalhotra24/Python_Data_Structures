""" Linked List implementation in Python. This implementation includes the following methods:
    1. Insert - Insert a new node into the list.
    2. Search - Search the list for the node that contains the requested data and return the node if found
    3. Delete - Search the list for the node that contains the requested data. If the node is found, remove
                from the list. 
"""

#! /usr/bin/python
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            new_node.next.prev = new_node
            self.head = new_node

    def search(self,k):
        current = self.head
        while current and current.next != None:
            if (current.data == k):
                return current
            else:
                current = current.next
        if (current.data == k):
            return current
        else:
            return None

    def print_list(self):
        current = self.head
        while current != None:
            print current.data
            current = current.next

# Main program
def main():
    list = LinkedList()
    # insert values into the linked list
    list.insert('1')
    list.insert('3')
    list.insert('4')
    list.insert('7')
    # print the values in the list
    list.print_list()

if __name__ == "__main__":
    main()