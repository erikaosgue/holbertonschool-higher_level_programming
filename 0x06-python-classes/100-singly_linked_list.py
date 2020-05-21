#!/usr/bin/python3
""" 7. Singly linked list """


class Node:
    """ Creates A New Node """
    __data = 0

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise Exception('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Creates the single Linked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value, self.__head)
            return

        if self.__head.next_node is None:
            if value < self.__head.data:
                self.__head = Node(value, self.__head)
            else:
                self.__head.next_node = Node(value, None)
            return

        prev = None
        curr = self.__head

        while curr and value > curr.data:
            prev = curr
            curr = curr.next_node

        if prev is None:
            self.__head = Node(value, self.__head)
        else:
            new_node = Node(value, prev.next_node)
            prev.next_node = new_node

    def __str__(self):
        curr = self.__head
        s = ''
        while curr:
            s += str(curr.data) + '\n'
            curr = curr.next_node
        if s and s[-1] == "\n":
            s = s[:-1]
        return s
