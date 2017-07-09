#!/usr/bin/env python3


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None
    

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node

    def append(self, data):
        node = Node(data)
        if self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def search(self, data):
        node = self.head
        if node is not None:
            while node.next is not None:
                if node.data == data:
                    return node
                node = node.next
            if node.data == data:
                return node

    def remove(self, node):
        if node is not self.head:
            node.prev.next = node.next
        else:
            node.next.prev = None
            self.head = node.next
        if node is not self.tail:
            node.next.prev = node.prev
        else:
            node.prev.next = None
            self.tail = node.prev

    def __str__(self):
        s = ""
        node = self.head
        if node is not None:
            s = str(node.data)
            while node.next is not None:
                node = node.next
                s += " " + str(node.data)
        return s


if __name__ == "__main__":
    l = LinkedList()
    l.append(1)
    print(l)
    l.append(2)
    print(l)
    l.append(3)
    print(l)
    l.append(4)
    print(l)
    l.append(5)
    print(l)
    l.remove(l.search(3))
    print(l)
    l.remove(l.search(5))
    print(l)
    l.remove(l.search(1))
    print(l)
    l.prepend(1)
    print(l)
    l.prepend(3)
    print(l)
    l.prepend(5)
    print(l)
