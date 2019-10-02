#!/usr/bin/python3
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:

    def __init__(self):
        self.__head = None
    """
    def __str__(self):
        result = ""
        node = self.__head
        if node != None:
            result += str(node.data)
            node = node.next_node
            while node is not None:
                result += "\n" + str(node.data)
                node = node.next_node
        result += ""
        return result
    """

    def __str__(self):
        result = []
        node = self.__head
        while node is not None:
            result.append(node.data)
            node = node.next_node
        new_list = sorted(result)
        result = "".join(str(x) + "\n" for x in new_list)
        result = result[:-1]
        return result

    def sorted_insert(self, value):
        new_node = Node(value, None)
        if self.__head is None:
            self.__head = new_node
            return None
        current_node = self.__head
        while current_node is not None:
            if current_node.next_node is None:
                current_node.next_node = new_node
                return None
            current_node = current_node.next_node
