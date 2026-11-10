from dataclasses import dataclass
from typing import Optional

@dataclass(slots=True,frozen=False,init=True,kw_only=True)
class Node:
    Data: int 
    Next: Optional['Node'] = None

# Linked List
# - IsEmpty()
# - Size()
# - InsertFront(data)
# - InsertBack(data)
# - InsertAt(data, position)
# - DeleteFront()
# - DeleteBack()
# - DeleteAt(position)
# - DeleteValue(data)


@dataclass(slots=True,frozen=False,init=True,kw_only=True)
class Linkedlist:
    head: Optional[Node]  = None
    size: int = 0

    def Display(self)->None:
        curr = self.head
        while curr:
            print(curr.Data,end=" -> ")
            curr = curr.Next
        print("None")

    def IsEmpty(self)->bool:
        # If head is None -> True // Empty 
        return self.head is None

    def Size(self)->int:
        counter:int = 0
        curr = self.head
        while curr:
            counter+=1
            curr = curr.Next
        return counter



    def InsertFront(self,value):
        node = Node(Data=value,)
        node.Next = self.head
        self.head = node
        self.size += 1


    def InsertBack(self,value)->None:
        node = Node(Data=value)
        if self.IsEmpty(): 
            self.head = node
        else:
            curr = self.head
            while curr.Next is not None:
                curr = curr.Next
            curr.Next = node
            self.size+=1


    def InsertAt(self,value,position):
        if position==-1 or position==self.Size():
            self.InsertBack(value)
            return
        
        if position<0 or position>self.Size():
            raise ValueError("Index out of Range")
        
        if position==0:
            self.InsertFront(value=value)
            return
        else:
            node = Node(Data=value)
            current = self.head
            for _ in range(position-1):
                current = current.Next
            node.Next = current.Next
            current.Next = node
            self.size+=1

    def DeleteFront(self):
        if self.IsEmpty():
            raise ValueError("Empty Linkedlist can't be deleted!")
        self.head = self.head.Next
        self.size -=1
    

    def DeleteBack(self):
        if self.IsEmpty():
            raise ValueError("Empty Linkedlist can't be deleted!")
        elif self.head.Next is None:
            self.head = None
            self.size = 0
        else:
            current = self.head
            # Because we need second last node, do delete the reference 
            while current.Next.Next is not None:
                current = current.Next
            current.Next = None
            self.size -=1 
        

    def DeleteAt(self,position):
        if self.IsEmpty(): 
            raise ValueError("Empty Linkedlist can't be deleted!")

        if position==-1 or position==self.Size()-1: 
            self.DeleteBack()
            return
        
        if position<0 or position>=self.Size(): 
            raise ValueError("Index out of Range")
        
        if position==0: 
            self.DeleteFront()
            return
        
        else:        
            current = self.head
            for _ in range(position-1):
                current = current.Next
            current.Next = current.Next.Next       
            self.size -= 1
        


    def Search(self,value)->tuple[int,bool]:
        if self.IsEmpty(): return (-1,False)
        current = self.head
        position = 0 
        while current is not None:
            if current.Data==value:
                return (position,True)
            current= current.Next
            position += 1
        return(-1,False)

    def RecursiveReverse(self):
        #TODO: Implementation
        ...

        

    def Reverse(self):
        if self.IsEmpty():
            raise ValueError("Linkedlist is Empty")
        
        previous = None 
        current = self.head

        while current is not None:
            next  = current.Next      # SAVE
            current.Next = previous   # Reverse
            # Move
            previous = current
            current = next

        self.head = previous





    def Get(self,position:int)->tuple[int,bool]:
        if position<0 or position>self.Size():
            raise ValueError("Index out of range")
        current = self.head 
        for  _ in range(position):
            current = current.Next 
        return current.Data
          

if __name__=="__main__":
    ll = Linkedlist()

    # Insert
    ll.InsertFront(20)
    ll.InsertFront(10)
    ll.InsertBack(30)
    ll.InsertAt(25, 2)

    ll.Display()
    # 10 -> 20 -> 25 -> 30

    # Search
    print(ll.Search(30))
    # (3, True)

    # Get
    print(ll.Get(0))
    # 10

    # Delete
    ll.DeleteAt(2)
    ll.Display()

    # 10 -> 20 -> 30

    ll.DeleteFront()
    ll.DeleteBack()

    ll.Display()
    # 20

    # Reverse
    ll.InsertBack(30)
    ll.InsertBack(40)
    ll.InsertAt(230,0)

    ll.Display()

    ll.RecursiveReverse()
    ll.Display()
            
    ll.Reverse()

    ll.Display()
    # 40 -> 30 -> 20