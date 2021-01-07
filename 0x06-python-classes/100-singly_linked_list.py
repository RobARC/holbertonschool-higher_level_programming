#!/usr/bin/python3
"""
Single Linked List module
Contains functions to create a basic singly linked list
"""


class Node:
    """
    Define a Node of a single linked list
    """

    def __init__(self, data, next_node=None):
        """
        Method to initializate a Node object
        """

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        method to getter data
        """

        return self.__data

    @data.setter
    def data(self, value):
        """
        method to setter data
        """

        error = "data must be an integer"
        if data != int:
            raise TypeError(error)
        self.__data = value

    @property
    def next_node(self):
        """
        method to getter next_node
        """

        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        method to setter next_node
        """

        error1 = "next_node must be a Node object"
        if value is not None and type(value) is not Node:
            raise TypeError(error1)
        self.__next_node = value


class SinglyLinkedList:
    """
    Defining a class single linked list
    """

    def __init__(self):
        """
        Method to initializate a SLL, starts empty
        """

        self.__head = None

    def __str__(self):
        """
        Return list of Nodes
        """

        NNode = self.__head
        List = []

        while NNode:
            List.append(str(NNode.data))
            NNode = NNode.next_node
        return("\n".join(List))

    def sorted_insert(self, value):
        """
        Insert a new node in numerical orden
        """

        NNode = self.__head
        error2 = "data must be an integer"
        if not isinstance(value, int):
            raise TypeError(error2)
        if NNode is None:
            self.__head = Node(value)
            return
        elif value < NNode.data:
            self.__head = Node(value, NNode)
            return
        while NNode:
            if not NNode.next_node:
                NNode.next_node = Node(value)
                break
            if value < NNode.next_node.data:
                NNode.next_node = Node(value, NNode.next_node)
                break
            NNode = NNode.next_node
