#!/usr/bin/env python

class Stack_Node:

    def __init__(self,payload = None, child = None):
        self.payload = payload
        self.child = child

    def get_child(self):
        return self.child

    def get_payload(self):
        return self.payload

    def set_child(self, data):
        self.child = data

    def set_payload(self, payload):
        self.payload = payload


class Stack:

    def __init__(self):
        self.root = None

    def push(self, data):
        newNode = Stack_Node(data)
        if self.root == None:
            self.root = newNode
        else: 
            newNode.set_child(self.root)
            self.root = newNode

    def pop(self):
        if self.root == None:
            return None
        else: 
            toReturn = self.root
            self.root = self.root.get_child()
            return toReturn.get_payload()
    def is_empty(self):
        return self.root == None

while not stack.is_empty():
    print(stack.pop())
