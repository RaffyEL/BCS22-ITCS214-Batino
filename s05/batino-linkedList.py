'''
	linked-list
		- is basically a data structure for storing collection of data or items

		class Box{
			int data
			Box next
		}

		head.data
			- the data - head is represents the first box
		box next
			- reflects to the next box that is connected to a particular box
'''

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None
		self.temporary = None

	def insert(self, data):
		new_node = Node(data)

		if self.head is None:
			self.head = new_node
		else:
			current = self.head
			while current.next:
				current = current.next
			if data == input_values[1]:
				self.temporary = new_node
			else:
				current.next = new_node

	def display(self):
		current = self.head
		while current:
			if current.data == input_values[2]:
				print(current.data, end=" -> ")
				current = current.next
				print(self.temporary.data, end=" -> ")
			else:
				print(current.data, end=" -> ")
				current = current.next
		print("None")

#input values
input_values = [6, 3, 4, 2, 1]
my_linked_list = LinkedList()
for value in input_values:
	my_linked_list.insert(value)

#display the linked list
my_linked_list.display()
