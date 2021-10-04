# Python3 implementation to reverse a
# doubly circular linked list
import math

# structure of a node of linked list
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# function to create and return a new node
def getNode(data):
	newNode = Node(data)
	newNode.data = data
	return newNode

# Function to insert at the end
def insertEnd(head, new_node):
	
	# If the list is empty, create a single node
	# circular and doubly list
	if (head == None) :
		new_node.next = new_node
		new_node.prev = new_node
		head = new_node
		return head
	
	# If list is not empty

	# Find last node
	last = head.prev

	# Start is going to be next of new_node
	new_node.next = head

	# Make new node previous of start
	head.prev = new_node

	# Make last previous of new node
	new_node.prev = last

	# Make new node next of old last
	last.next = new_node
	return head

# Utility function to reverse a
# doubly circular linked list
def reverse(head):
	if (head == None):
		return None

	# Initialize a new head pointer
	new_head = None

	# get pointer to the the last node
	last = head.prev

	# set 'curr' to last node
	curr = last
	#*prev

	# traverse list in backward direction
	while (curr.prev != last):
		prev = curr.prev

		# insert 'curr' at the end of the list
		# starting with the 'new_head' pointer
		new_head = insertEnd(new_head, curr)
		curr = prev
	
	new_head = insertEnd(new_head, curr)

	# head pointer of the reversed list
	return new_head

# function to display a doubly circular list in
# forward and backward direction
def display(head):
	if (head == None):
		return
	
	temp = head

	print("Forward direction: ", end = "")
	while (temp.next != head):
		print(temp.data, end = " ")
		temp = temp.next
	
	print(temp.data)

	last = head.prev
	temp = last

	print("Backward direction: ", end = "")
	while (temp.prev != last):
		print(temp.data, end = " ")
		temp = temp.prev
	
	print(temp.data)

# Driver Code
if __name__=='__main__':

	head = None

	head = insertEnd(head, getNode(1))
	head = insertEnd(head, getNode(2))
	head = insertEnd(head, getNode(3))
	head = insertEnd(head, getNode(4))
	head = insertEnd(head, getNode(5))

	print("Current list:")
	display(head)

	head = reverse(head)

	print("\nReversed list:")
	display(head)

# This code is contributed by Srathore
