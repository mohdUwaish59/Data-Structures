from Node_Creation import Node 

class Linked_List:
    def __init__(self):
        self.head=None
        self.tail=None

    def insert_Beginning(self, val):
        newNode = Node(val)
        if self.head != None:
            newNode.link=self.head
            self.head=newNode
        else:
            self.head=newNode
            self.tail=newNode

    def insert_Nth(self, val,pos):
        newNode = Node(val) 
        if(pos < 1):
           print("\nposition should be >= 1.")
        elif (pos == 1):
         newNode.link = self.head
         self.head = newNode
        else:    
          temp = self.head
        for i in range(1, pos-1):
         if(temp != None):
              temp = temp.link  
         if(temp != None):
            newNode.link = temp.link
            temp.link = newNode  
        else:
            print("\nThe previous node is null.")

    def insert_Last(self, val):
        '''O(N)'''
        newNode = Node(val)
        current =self.head
        if self.head != None:
            while current.link!=None:
                current = current.link
            current.link = newNode
        else:
            self.head=newNode

    def insert_Last_C(self,val):
        '''Not working'''
        newNode=Node(val)
        self.tail.next = newNode
        self.tail = newNode

    def delete(self, ele):
        if self.head==None:
            print("List is Empty")
            return
        if self.head.val==ele:
            temp=self.head
            self.head=temp.link
            temp=None
            return
        current=self.head
        while current.link!=None:
            if current.link.val==ele:
                temp=current.link
                current.link=temp.link
                temp=None
                return
            current=current.link
        print("Element not found")

    def shift_Nth_to_first(self,pos):
        if pos<1:
            print("invalif position")
            return
        else:
            current=self.head
            for i in range(1,pos-1):
                current=current.link
            temp=current.link
            current.link=temp.link
            temp.link=self.head
            self.head=temp
            return

    def display(self):
        if self.head==None:
            print("List is empty")
            return
        current = self.head
        while current != None:
            print(current.val)
            current=current.link
           
LL = Linked_List()
LL.insert_Beginning(25)
LL.insert_Beginning(35)
LL.insert_Beginning(45)
LL.insert_Beginning(55)
LL.insert_Beginning(65)
LL.insert_Beginning(100)
LL.shift_Nth_to_first(4)
LL.display()