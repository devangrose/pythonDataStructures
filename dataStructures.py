#!/usr/bin/env python


class Linked_List_Node:

    def __init__(self, payload, parent = None, child = None):
        self.payload = payload
        self.parent = parent
        self.child = child

    def has_child(self):
        return not self.child == None

    def has_parent(self):
        return  not self.parent == None

    def get_child(self):
        if self.has_child():
            return self.child
        else: return None

    def set_child(self, child):
        self.child = child

    def get_parent(self):
        if self.has_parent():
            return self.parent
        else: return None

    def set_parent(self, parent):
        self.parent = parent
    
    def get_payload(self):
        return self.payload

    def set_payload(self, payload):
        self.payload = payload

class Linked_List:
    
    def __init__(self):
        self.head = None

    def __len__(self):
        toReturn = 0
        current_node = self.head
        while not current_node == None:
            toReturn += 1
            current_node = current_node.get_child()
        return toReturn

    def add(self, data):

        # make new node
        newNode = Linked_List_Node(data)
        # case - List is empty
        if self.head == None:
            self.head = newNode
        # case - List is not empty
        else: 
            current_node = self.head
            
            # traverse through list to end
            while current_node.has_child():
                current_node = current_node.get_child()
            
            # insert into list
            current_node.set_child(newNode)
            newNode.set_parent(current_node)

    def find_in_list(self,term):
        current_node = self.head
        # traverse the list until end or match
        while (not current_node.get_payload() == term) and current_node.has_child():
            print "checking {} vs {}".format(current_node.get_payload(),term)
            current_node = current_node.get_child()
            print current_node.get_payload()
        if current_node.get_payload() == term:
            return current_node
        else: return None

    def delete(self, term):
        
        # find the node in the list
        node = self.find_in_list(term) 
        if not node == None:    
            parent = node.get_parent()
            child = node.get_child()
            
            # top of list
            if parent == None:

                # last in list
                if child == None:
                    self.head = None
                else:
                    self.head = child
            else: 
                
                # last in list
                if child == None:
                    parent.set_child(None)
                else:
                    child.set_parent(parent)
                    parent.set_child(child)
        else: print "Item not in list"

    def get_item(self,term):
        node = self.find_in_list(term)

        if node == None: 
            return  None
        else: return node.get_payload()

    def print_list(self):
        current_node = self.head
        if not current_node == None:
            print current_node.get_payload(),
            current_node = current_node.get_child()
        while not current_node == None:
            print ", ",
            print current_node.get_payload(),
            
            current_node = current_node.get_child()
    
    def pop(self):
        if not self.head == None:
            toReturn = self.head.get_payload()
            self.head = self.head.get_child()
            return toReturn
        else: return None


