#Creating a Node class
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


#Class for Single linked list
class SinglyLinkedList:

    def __init__(self):
        self.head = None

    #INSERTING FUNCTIONS
    def insertAtFirst(self,data):       
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insertAtLast(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current=current.next
            current.next = new_node
    
    def insertAtLoc(self,data,pos):
        if pos < 0:
            raise ValueError("Position can't be a negative number!")
        
        new_node = Node(data)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        for _ in range(pos-1):
            if current is None:
                raise IndexError("Position out of range!")
            current = current.next

        new_node.next = current.next
        current.next = new_node

    #DELETING FUNCTIONS
    def deleteAtFirst(self):
        if self.head is not None:
            self.head = self.head.next
        else:
            print("No Elements are found!")
            return

    def deleteAtLast(self):
        if self.head is None:
            print("No elements in the list!")
            return
        elif self.head.next is None:
            self.head = None
            return
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None

    def deleteAtLoc(self,pos):
        if pos < 0:
            raise ValueError("Position can't be a negative number!")
        
        if self.head is None:
            print("No Elements are in the list!")
            return
        
        if pos == 0:
            self.head = self.head.next
            return
        
        current = self.head
        for _ in range(pos-1):
            if current.next is None:
                raise IndexError("Position out of bound!")
            current = current.next

        if current.next is None:
            raise IndexError("Position out of bound!")
        current.next = current.next.next

    def display(self):
        current = self.head
        while current:
            print(current.data,end="->")
            current = current.next
        print("NULL")
    
inp=int(input(("Choose one:\n1-Open a Single Linked List\n2-Exit\n")))
if inp == 1:
    sll = SinglyLinkedList()
else:
    exit()

while True:
    ch = int(input("Enter your Choice:\n1:Insert at first\n2:Insert at last\n3:Insert at location\n4:Delete at first\n5:Delete at last\n6:Delete at location\n7:Display\n8:Exit\n"))
    if ch == 1:
        in1 = int(input("Enter the number to be inserted:"))
        sll.insertAtFirst(in1)
    elif ch == 2:
        in1 = int(input("Enter the number to be inserted:"))
        sll.insertAtLast(in1)
    elif ch == 3:
        in1 = int(input("Enter the number to be inserted:"))
        in2 = int(input("Enter the location to be inserted:"))
        sll.insertAtLoc(in1,in2)
    elif ch == 4:
        sll.deleteAtFirst()
    elif ch == 5:
        sll.deleteAtLast()
    elif ch == 6:
        loc = int(input("Enter the location to delete:"))
        sll.deleteAtLoc(loc)
    elif ch == 7:
        sll.display()
    elif ch == 8:
        break
print("______END______")