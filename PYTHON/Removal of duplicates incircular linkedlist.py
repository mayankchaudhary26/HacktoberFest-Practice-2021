class Node:  
   def __init__(self,data):
      self.data = data
      self.next = None  

class list_creation:  
   def __init__(self):  
      self.head = Node(None)  
      self.tail = Node(None)  
      self.head.next = self.tail  
      self.tail.next = self.head  

   def add_data(self,my_data):  
      new_node = Node(my_data)
      if self.head.data is None:  
         self.head = new_node  
         self.tail = new_node  
         new_node.next = self.head  
      else:  
         self.tail.next = new_node
         self.tail = new_node
         self.tail.next = self.head

   def remove_duplicate_vals(self):  
      curr = self.head
      if(self.head == None):
         print("The list is empty")
      else:
         while(True):
            temp = curr
            index_val = curr.next
            while(index_val != self.head):
               if(curr.data == index_val.data):
                  temp.next = index_val.next
               else:
                  temp = index_val
                  index_val= index_val.next
            curr =curr.next
            if(curr.next == self.head):
               break;        
   def print_it(self):  
      curr = self.head
      if self.head is None:  
         print("The list is empty");  
         return;  
      else:
         print(curr.data)
         while(curr.next != self.head):  
            curr = curr.next
            print(curr.data)
         print("\n")

class circular_linked_list:  
   my_cl = list_creation()
   print("Nodes are being added to the list")
   my_cl.add_data(21)
   my_cl.add_data(54)
   my_cl.add_data(78)
   my_cl.add_data(99)
   my_cl.add_data(21)
   print("The list is :")
   my_cl.print_it();  
   my_cl.remove_duplicate_vals()
   print("The updated list is :")
   my_cl.print_it(); 
