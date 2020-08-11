class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def delete(self):
        if not self.head:
            print("No nodes")
        else:
            temp = self.head
            self.head = self.head.next
            return temp.data

    def print(self):
        if not self.head:
            print("The list is empty")
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
