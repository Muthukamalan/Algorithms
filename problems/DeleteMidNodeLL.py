from datastructures.linkedlist.singly import Linkedlist,Node


def RemoveMidNode0(head:Node)->Node:
    """
    1 → 2 → 3 → 4 → 5 → None       =>   1 → 2 → 4 → 5 → None
    1 → 2 → 3 → 4 → 5 → 6 → None   =>   1 → 2 → 4 → 5 → 6 → None
    """
    if head is None or head.Next is None:
        return None
    
    slow = head 
    fast = head
    prev = None 

    while ( (fast is not None) and (fast.Next is not None) ) :
        prev = slow
        slow = slow.Next
        fast = fast.Next.Next

    prev.Next = slow.Next
    return head



# remove the second middle node in an even-length linked list.
def RemoveMidNode(head:Node)->Node:
    """
    1 → 2 → 3 → 4 → 5 → None       =>   1 → 2 → 4 → 5 → None
    1 → 2 → 3 → 4 → 5 → 6 → None   =>   1 → 2 → 3 → 5 → 6 → None
    """
    if head is None or head.Next is None:
        return None
    
    slow = head 
    fast = head.Next 

    while ( (fast is not None) and (fast.Next is not None) ) :
        slow = slow.Next
        fast = fast.Next.Next

    slow.Next = slow.Next.Next
    return head


def RemoveMidNode1(head:Node)->Node:
    """
    1 → 2 → 3 → 4 → 5 → None       =>   1 → 2 → 4 → 5 → None
    1 → 2 → 3 → 4 → 5 → 6 → None   =>   1 → 2 → 4 → 5 → 6 → None
    """
    if head is None or head.Next is None:
        return None
    
    slow = head 
    fast = head.Next 

    while ( (fast.Next is not None) and (fast.Next.Next is not None) ) :
        slow = slow.Next
        fast = fast.Next.Next

    slow.Next = slow.Next.Next
    return head
