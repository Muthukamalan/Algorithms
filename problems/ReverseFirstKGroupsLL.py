from datastructures.linkedlist.singly import Linkedlist,Node

def reverseLinkedList(head: Node) -> Node:
    prev = None
    current = head

    while current:
        newNext = current.Next
        current.Next = prev

        prev = current
        current = newNext

    return prev



def ReverseFirstKGroups(head:Node, k:int):
    if head is None or k<2:
        return head

    kthNode = head 
    count = 1

    while kthNode and count<k:
        kthNode = kthNode.Next
        count+=1

    if kthNode is None:
        return reverseLinkedList(head)

    nextNode = kthNode.Next
    kthNode.Next = None

    newHead = reverseLinkedList(head)
    head.Next = nextNode


    return newHead


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

    linkly.head= ReverseFirstKGroups(linkly.head,4)
    linkly.Display()