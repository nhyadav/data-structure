class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)



# insert the data in sorted doubly linked list
def insert_data_dlinkedlist(dllist, data):
    newnode = DoublyLinkedListNode(data)
    if dllist is None:
        return newnode
    elif dllist.data >= newnode.data:
            newnode.next = dllist
            newnode.next.prev = newnode
            dllist = newnode
    else:
        current = dllist
        while ((current.next) and
                (current.next.data < newnode.data)):
            current = current.next
        newnode.next = current.next
        if current.next is not None:
            newnode.next.prev = newnode

        current.next = newnode
        newnode.prev = current
    return dllist

def reverse_doubly_linkedlist(dllist):
    if not dllist:
        return dllist
    dllist.next, dllist.prev = dllist.prev, dllist.next
    if not dllist.prev:
        return dllist
    return reverse(dllist.prev)
