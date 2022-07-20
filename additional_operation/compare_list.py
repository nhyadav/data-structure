
def compare_list(list1, list2):
    """both the list should be atleast one data"""
    while list or list2:
        if list1 and list2:
            if list1.data==list2.data:
                list1 = list1.next
                list2 = list2.next
            else:
                return 0
        else:
            return 0
    return 1

def merged_two_sorted_list(list1, list2):
    start = nodeobj
    temp = start
    while True:
        if list1 is None and list2 is None:
            return None
        if list1 is None:
            temp.next = list2
        if list2 is None:
            temp.next = list1
        if list1.data <= list2.data:
            temp.next = list1
            list1 = list1.next
        else:
            temp.next = list2
            list2 = list2.next
    return start.next
    """Meged two sorted linked list:"""

def get_node_value(llist, positinfromtail):
    if not llist:
        return None
    else:
        tortose = llist
        hare = llist
        for i in range(positionFromTail):
            hare = hare.next
        while hare.next!=None:
            tortose = tortose.next
            hare = hare.next
        return tortose.data
    """get the values from tails"""
def remove_duplicate_from_sorted_llist(llist):
    if not llist:
        return None
    else:
        turtose = llist
        hare = llist.next
        while hare:
            if turtose.data == hare.data:
                hare = hare.next
                turtose.next = hare
            else:
                turtose = turtose.next
                hare = hare.next
        return llist
    """REmove the duplicate data from the node"""

def cycle_detection(llist):
    if not llist:
        return None
    else:
        turtoise = llist
        hare = llist
        while hare!=None and hare.next!=None:
            hare = hare.next.next
            turtoise = turtoise.next.next
            if hare==turtoise:
                return 1
        return 0
    """detectinf the cycle from the linked list"""
    

def find_merged_point_lists(llist1, llist2):
    lista = llist1
    listb = llist2
    while lista!=listb:
        if lista.next==None:
            lista = llist2
        else:
            lista = lista.next
        if listb.next == None:
            listb = llist1
        else:
            listb = listb.next
    return listb.data
    """Find the merged point of the 1 linked list"""