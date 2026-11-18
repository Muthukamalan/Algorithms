from datastructures.linkedlist.singly import Linkedlist,Node 


def getKthNode(node:Node,k:int)->Node:
    k -= 1
    while node and k > 0:
        node = node.Next
        k-=1
    return node 


def reverseLinkedList(head:Node)->Node:
    prev = None
    current = head 

    while current:
        newNext = current.Next
        current.Next = prev

        prev = current
        current = newNext
    return prev

def ReverseAllKGroups(head:Node, k:int):
    if head is None     or k<=1:
        return head 


    prev:Node = None
    temp = head

    while temp:
        kthNode = getKthNode(temp,k=k)

        if kthNode is None:
            if prev:
                prev.Next = temp 
            break

        nextNode = kthNode.Next
        kthNode.Next = None

        reverseLinkedList(temp)

        if temp==head:
            head=kthNode
        else:
            prev.Next = kthNode


        prev=temp
        temp = nextNode

    return head

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

    linkly.head = ReverseAllKGroups(linkly.head,6)
    linkly.Display()