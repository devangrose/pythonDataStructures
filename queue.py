#!/usr/bin/env python


class Queue_Node:

    def __init__(self, payload = None,parent = None, child = None):
        self.payload = payload
        self.child = child
        self.parent = parent
    def get_payload(self):
        return self.payload

    def set_payload(self, data):
        self.payload = data

    def get_child(self):
        return self.child

    def set_child(self, data):
        self.child = data
    
    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

class Queue:

    def __init__(self):
        self.root = None

    def enqueue(self, data):
        newNode = Queue_Node(data)
    
        # case - First Node
        if self.root == None:
            self.root = newNode
        else: 
            newNode.set_child(self.root)
            self.root.set_parent(newNode)
            self.root = newNode

    def dequeue(self):

        if self.root == None:
            return None

        else: 
            current_node = self.root
            while not current_node.get_child() == None:
                current_node = current_node.get_child()
            
            # last node
            if current_node.get_parent() == None:
                self.root = None
                return current_node.get_payload()
            else: 
                current_node.get_parent().set_child(None)
                return current_node.get_payload()
    
    def is_empty(self):
        return self.root == None
class Easy_Queue:

    def __init__(self):
        self.data = []

    def enqueue(self, data):
        self.data.insert(0,data)
    
    def dequeue(self):
        return self.data.pop()


