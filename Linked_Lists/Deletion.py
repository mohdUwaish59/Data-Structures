from Node_Creation import Node 

class Linked_List:
    def __init__(self):
        self.head=None
    
    def delete(self, ele):
        if self.head==None:
            print("List is Empty")
            return
        elif self.head.val==ele:
            temp=self.head
            self.head=temp.link
            temp=None
            current=self.head
            while current.link!=None:
                if current.link.val==ele:
                    temp=current.link
                    current=temp.link
                    temp=None
                    return
                current=current.link
        
        print("Element not found")