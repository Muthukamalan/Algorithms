from datastructures.linkedlist.singly import Linkedlist,Node


def ReverseKLL(head:Node,k:int):
    prev = None 
    current  = head 

    while current and k>0:

        # save 
        newNext = current.Next
        # new connection
        current.Next = prev 
        # move forward
        prev = current
        current = newNext
        # counter
        k-=1

    # connect to orginal linkedlist
    head.Next = current
    # return new head
    return prev


if __name__=="__main__":
    linkly = Linkedlist()
    linkly.InsertBack(3)
    linkly.InsertBack(5)
    linkly.InsertBack(7)
    linkly.InsertBack(6)
    linkly.InsertBack(9)
    linkly.InsertBack(1)
    print("== Original LinkedList ==")
    linkly.Display()
    print("*"*10)

    linkly.head = ReverseKLL(linkly.head,4)
    linkly.Display()