#!/usr/bin/env python

class BST_Node:

    def __init__(self, payload, parent = None, left_child = None, right_child = None):
        self.payload = payload
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

    def get_payload(self):
        return self.payload

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def get_parent(self):
        return self.parent

    def set_payload(self, payload):
        self.payload = payload

    def set_left_child(self, child):
        self.left_child = child

    def set_right_child(self, child):
        self.right_child = child

    def set_parent(self, parent):
        self.parent = parent

    def has_right_child(self):
        if self.right_child == None:
            return False
        return True

    def has_left_child(self):
        if self.left_child == None:
            return False
        return True

    def has_parent(self):
        if self.parent == None:
            return False
        return True

class BST:

    def __init__(self):
        self.head = None

    def put(self, data, current_node):
        if data < current_node.get_payload():
            if current_node.has_left_child():
                self.put(data, current_node.get_left_child())
            else:
                newNode = BST_Node(data)
                newNode.set_parent(current_node)
                current_node.set_left_child(newNode)

        elif data > current_node.get_payload():
            if current_node.has_right_child():
                self.put(data, current_node.get_right_child())
            else:
                newNode = BST_Node(data)
                newNode.set_parent(current_node)
                current_node.set_right_child(newNode)

    def add(self,data):
        newNode = BST_Node(data)
        if self.head == None:
            self.head = newNode
        else: 
            current_node = self.head
            self.put(data,current_node)

    def print_list_ascending(self):
       self._print_list_ascending(self.head)
    
    def _print_list_ascending(self, current_node):
        if current_node == None:
            return
        else: 
            if current_node.has_left_child():
                self._print_list_ascending(current_node.get_left_child())
            print current_node.get_payload(),
            if current_node.has_right_child():
                self._print_list_ascending(current_node.get_right_child())

bstlist = BST()
bstlist.add(1)
bstlist.add(2)
bstlist.add(0)
bstlist.add(3)

bstlist.print_list_ascending()
