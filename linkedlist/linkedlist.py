# create a linkedlistnode

class SingleLinkedListNode:
    def __init__(self, n_data):
        self.data = n_data
        self.next = None  # return the node with data and null in next

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_node_linkeedlist(self, data):
        node = SingleLinkedListNode(data)
        if self.head:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        """Insert a node  in to singlylinkedlist"""

    def traverse_linkedlist(self):
        if self.head:
            temp = self.head
            while temp:
                print(temp.data)
                temp = temp.next
        else:
            return None
        """Traverse the linkedlist"""

    def insertNodeAtTail(self, data):
        node = SingleLinkedListNode(data)
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
        else:
            self.head = node
        """Add node at the tail of the linked list"""

    def insertNodeAtHead(self, data):
        node = SingleLinkedListNode(data)
        if not self.head:
            self.head = node
        else:
            temp = self.head
            node.next = temp
            temp = node
            self.head = temp
        """Insert data at the head part"""

    def insertNodeAtPosition(self, data, position):
        if not self.head:
            return None
        else:
            node = SingleLinkedListNode(data)
            prev = self.head
            temp = self.head.next
            for i in range(position-1):
                prev = prev.next
                temp = temp.next
            prev.next = node
            node.next = temp
        """Insert data at position"""

    def delete_node(self,position):
        if not self.head:
            return None
        elif position==0:
            temp = self.head.next
            self.head = temp
        else:
            turtose = self.head
            hare = self.head.next.next
            for i in range(position-1):
                turtose = turtose.next
                hare = hare.next
            turtose.next = hare
        """Delete the node at position"""

    def reverse_print(self, head):
        if not head:
            return None
        else:
            self.reverse_print(head.next)
            print(head.data)
        """Reverse the Linked List"""

    def reversed_linked_list(self):
        if not self.head:
            return None
        else:
            temp = None
            nextnode = None
            while self.head:
                nextnode = self.head.next
                self.head.next = temp
                temp = self.head
                self.head = nextnode
            while temp:
                print(temp.data)
                temp = temp.next
            #return temp





## test the code
if __name__ == '__main__':
    list_count = int(input("Enter the Linkedlist node counts:"))
    linkedlist = SinglyLinkedList()
    for _ in range(list_count):
        list_node_data = int(input("Enter the node data:"))
        linkedlist.insert_node_linkeedlist(list_node_data)
    print("linkedlist data")
    linkedlist.traverse_linkedlist()
    print(" Add the node at the tail")
    #tnode = int(input("Enter the tnode data:"))
    #linkedlist.insertNodeAtTail(tnode)
    #print("Linkedlist after adding data at the tail")
   # linkedlist.traverse_linkedlist()
    #print(" Add the node at the head")
    #hnode = int(input("Enter the tnode data:"))
    ##linkedlist.insertNodeAtHead(hnode)
    #print("Linkedlist after adding data at the head")
    #linkedlist.traverse_linkedlist()
    #print(" Add the node at the position")
    #pnode = int(input("Enter the data:"))
    #position = int(input("Enter the position:"))
    #linkedlist.insertNodeAtPosition(pnode, position)
    #print("Linkedlist after adding data at the position:")
    #linkedlist.traverse_linkedlist()
    #print(" Delete the node at the position")
    #position = int(input("Enter the position:"))
    #linkedlist.delete_node(position)
    #print("Linkedlist after deletion data data at the position:")
    #linkedlist.traverse_linkedlist()
    print("Reverse of the LinkedList")
    #linkedlist.reverse_print(linkedlist.head)
    linkedlist.reversed_linked_list()