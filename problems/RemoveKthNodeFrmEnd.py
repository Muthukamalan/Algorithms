from datastructures.linkedlist.singly import Node,Linkedlist

def removeNthFromEnd(ll:Linkedlist,n:int):
    # A:: Head Node
    # n:: integer

    """
    if n=N-1, then Removing the head node will lost ( so keep sentinal node to preserve from happening)
    """

    if n<=0 or n>ll.Size():
        return ll.head

    dummy = Node(0)
    dummy.Next = ll.head

    slow = ll.head
    fast = ll.head

    while n>0:
        fast = fast.Next

    while fast.Next is not None:
        slow = slow.Next
        fast = fast.Next

    slow = slow.Next

    return dummy.Next
