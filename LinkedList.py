
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
  
# Constructor to initialize the node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # Method to print linked list 
    def printList(self): 
        temp = self.head 
        
          
        while temp : 
            print(temp.data,end= "->") 
            temp = temp.next
  
    # Function to add of node at the end. 
    def appendAtBegin(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        
        
        
    def appendAtEnd(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
        
            while current.next is not None:
                current = current.next
            current.next = newNode
        

def mergeList(head1,head2):
    temp = None
    
    if head1 is None: 
        return head2 

    if head2 is None: 
        return head1 
    
    if (head1.data <= head2.data):
        temp = head1
        temp.next = mergeList(head1.next,head2)
    else: 
        temp = head2
        temp.next = mergeList(head1,head2.next)
    
    return temp


def detectCycle( A):
        if A is None:
            return
        hM = {}
        result = A
        while A is not None:
            if (hM.get(A.data) >= 1):
                hM[A.data] += 1
            else:
                hM[A.data] = 1
        
            if (hM.get(A.data) == 2):
                result = A
                break
            
            A = A.next
        return A.data

def deleteDuplicates( A):
        if A is None:
            return
        hM = {}
        head = A
        prev = Node
        check = True
       
        curr = A.next
        while A is not None and curr is not None:

                
            if ( head.data == curr.data and curr.next is None):
                head.next = None
                break
            
            if (A.data != curr.data):
                if (check == True):
                    head.next = A.next
                    prev = A.next
                    check = False
                else:
                    prev.next = A.next
                    prev = A.next
                
            if (  curr.next is None  ):
                prev.next = None
                break
        
            A = A.next
            curr = A.next
            
        return head

    

list1 =  LinkedList()
list1.appendAtEnd(20)
list1.appendAtEnd(30)
list1.appendAtEnd(40)
list1.appendAtEnd(20)
list1.appendAtBegin(10)
list1.appendAtBegin(5)


list2 =  LinkedList()
list2.appendAtEnd(11)
list2.appendAtEnd(12)
list2.appendAtEnd(13)
list2.appendAtBegin(6)
list2.appendAtBegin(4)


duplicateList = LinkedList()

duplicateList.appendAtEnd(10)
duplicateList.appendAtEnd(10)
duplicateList.appendAtEnd(10)




list1.printList()
print ("\n")
list2.printList()
print ("\n")
list3 =  LinkedList()

list3.head = mergeList(list1.head,list2.head)

deleteDuplicates(duplicateList.head)

duplicateList.printList()

print("\n")

#print(detectCycle(list1.head))

list3.printList()



print("\n")
        
        

