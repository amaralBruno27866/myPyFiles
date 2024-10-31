#    Main Author(s): Bruno Amaral
#    Main Reviewer(s): Bruno Amaral




class SortedList:

	class Node:
		def __init__(self, data=None, next = None, prev = None):
			self.data = data # Data stored in the node
			self.next = next # Pointer to the next node
			self.prev = prev # Pointer to the previous node

		def get_data(self):
			return self.data # Returns the data stored in the node

		def get_next(self):
			return self.next # Returns the next node

		def get_previous(self):
			return self.prev # Returns the previous node

	def __init__(self):
		self.head = self.Node() # Sentinel node for head
		self.tail = self.Node() # Sentinel node for tail
		self.head.next = self.tail # Head points to tail
		self.tail.prev = self.head # Tail points
		self.size = 0 # Number of elements in the list

	def get_front(self):
		if self.is_empty(): # If the list is empty
			return None # Return None
		return self.head.get_next() # If not empty, the data stored in the first node

	def get_back(self):
		if self.is_empty(): # If the list is empty
			return None # Return None
		return self.tail.get_previous() # If not empty, the data stored in the last node

	def is_empty(self):
		return self.size == 0 # Returns True if the list is empty, False otherwise

	def __len__(self):
		return self.size # Returns the number of elements in the list

	def insert(self,data):
		new_node = self.Node(data) # Create a new node with the data
		current = self.head.get_next() # Start at the first node
		while current != self.tail and current.get_data() < data: # While the current node is not the tail and the data is smaller than the current node
			current = current.get_next() # Move to the next node
		previous = current.get_previous() # Get the previous node
		previous.next = new_node # The previous node points to the new node
		new_node.prev = previous # The new node points to the previous node
		new_node.next = current # The new node points to the current node
		current.prev = new_node # The current node points to the new node
		self.size += 1 # Increment the size
		return new_node # Return the new node

	def erase(self,node):
		if node is None: # If the node is None
			raise ValueError("Cannot erase node referred to by None") # Raise a ValueError
		if self.is_empty(): # If the list is empty
			return # Return
		prev_node = node.get_previous() # Get the previous node
		next_node = node.get_next() # Get the next node
		prev_node.next = next_node # The previous node points to the next node
		next_node.prev = prev_node # The next node points to the previous node
		self.size -= 1 # Decrement the size

	def search(self, data):
		current = self.head.get_next() # Start at the first node
		while current != self.tail: # While the current node is not the tail
			if current.get_data() == data: # If the data stored in the current node is equal to the data
				return current # Return the current node
			current =  current.get_next() # Move to the next node
		return None # Return None if the data is not found
