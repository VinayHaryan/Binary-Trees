# nodes from a sorted linked list
 
# Node class
class Node:
 
    # Constructor to initialize
    # the node object
    def __init__(self, data):
        self.data = data
        self.next = None
 
class LinkedList:
 
    # Function to initialize head
    def __init__(self):
        self.head = None
 
    # Function to insert a new node
    # at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

        
    # Utility function to print the
    # linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data , end = ' ')
            temp = temp.next
     
    # This function removes duplicates
    # from a sorted list        
    def removeDuplicates(self):
        temp = self.head
        if temp is None:
            return
        while temp.next is not None:
            if temp.data == temp.next.data:
                new = temp.next.next
                temp.next = None
                temp.next = new
            else:
                temp = temp.next
        return self.head
 
# Driver Code
llist = LinkedList()
 
llist.push(20)
llist.push(13)
llist.push(13)
llist.push(11)
llist.push(11)
llist.push(11)
print ("Created Linked List: ")
llist.printList()
print()
print("Linked List after removing",
             "duplicate elements:")
llist.removeDuplicates()
llist.printList()
