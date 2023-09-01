from Node_Creation import Node

class Doubly_Linked_List:
    def __init__(self):
       self.head=None
       self.tail=None

    # Insertion
      # At Beginning
      # At Last
      # At Nth
    def insert_At_Beginning(self, val):
        newNode=Node(val)
        if self.head==None:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.link=self.head
            self.head.prev=newNode.link
            self.head=newNode

    def display(self):
        print(f"The tail is pointing to {self.tail.val}")
        print(f"The head is pointing to {self.head.val}")
        if self.head==None:
            print("List is empty")
            return
        current = self.head
        while current != None:
            print(current.val)
            current=current.link


LL=Doubly_Linked_List()
LL.insert_At_Beginning(5)
LL.insert_At_Beginning(15)
LL.insert_At_Beginning(25)
LL.insert_At_Beginning(35)
LL.insert_At_Beginning(45)
LL.insert_At_Beginning(55)
LL.insert_At_Beginning(65)
LL.insert_At_Beginning(75)

LL.display()


