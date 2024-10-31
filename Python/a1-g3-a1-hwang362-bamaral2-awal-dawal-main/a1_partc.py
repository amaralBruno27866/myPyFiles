#    Main Author(s): Bruno Amaral
#    Main Reviewer(s): Bruno Amaral



class Stack:

	def __init__(self, cap = 10): # Stack with fixed capacity
		self.cap = cap # Capacity
		self.data = [None] * cap # Data
		self.size = 0	# Size

	def capacity(self):
		return self.cap # Return capacity

	def push(self, data):
		if self.size >= self.cap: # If size is greater than or equal to capacity
			self._resize() # Resize
		self.data[self.size] = data # Data size is data
		self.size += 1 # Size is size plus 1

	def pop(self):
		if self.is_empty(): # If is empty
			raise IndexError("pop() used on empty stack") # Raise index error
		top = self.data[self.size - 1] # Top is data size minus 1
		self.data[self.size - 1] = None # Data size minus 1 is none
		self.size -= 1 # Size is size minus 1
		return top # Return top

	def get_top(self):
		if self.is_empty(): # If is empty
			return None # Return none
		return self.data[self.size - 1] # Return data size minus 1

	def is_empty(self):
		return self.size == 0 # Return size is equal to 0

	def __len__(self):
		return self.size # Return size
	
	def _resize(self): # This function is used to resize the stack
		self.cap *= 2 # Capacity is capacity times 2
		new_data = [None] * self.cap # New data is none times capacity
		for i in range(self.size): # For i in range size
			new_data[i] = self.data[i] # New data i is data i
		self.data = new_data # Data is new data

# Bruno's implementation
class Queue:

	def __init__(self, cap = 10): # Circular array
		self.cap = cap # Capacity
		self.data = [None] * cap # Data
		self.size = 0 # Size
		self.front = 0 # Front
		self.rear = 0 # Rear

	def capacity(self):
		return self.cap # Return capacity

	def enqueue(self, data):
		if self.size >= self.cap: # If size is greater than or equal to capacity
			self._resize() # Resize
		self.data[self.rear] = data # Rear is data
		self.rear = (self.rear + 1) % self.cap # Rear is rear plus 1 mod capacity
		self.size += 1 # Size is size plus 1

	def dequeue(self):
		if self.is_empty(): # If is empty
			raise IndexError("dequeue() used on empty queue") # Raise index error
		front_data = self.data[self.front] # Front data is data front
		self.data[self.front] = None # Data front is none
		self.front = (self.front + 1) % self.cap # Front is front plus 1 mod capacity
		self.size -= 1 # Size is size minus 1
		return front_data # Return front data

	def get_front(self):
		if self.is_empty(): # If is empty
			return None # Return none
		return self.data[self.front] # Return data front

	def is_empty(self):
		return self.size == 0 # Return size is equal to 0

	def __len__(self):
		return self.size # Return size
	
	def _resize(self): # This function is used to resize the queue
		new_cap = self.cap * 2 # New capacity is capacity times 2
		new_data = [None] * new_cap # New data is none times new capacity
		for i in range(self.size): # For i in range size
			new_data[i] = self.data[(self.front + i) % self.cap] # New data i is data front plus i mod capacity
		self.data = new_data # Data is new data
		self.cap = new_cap # Capacity is new capacity
		self.front = 0 # Front is 0
		self.rear = self.size # Rear is size
		self.cap = new_cap # Capacity is new capacity


class Deque:

	def __init__(self, cap = 10): # Circular array
		self.cap = cap # Capacity
		self.data = [None] * cap # Data
		self.size = 0 # Size
		self.front = 0 # Front
		self.rear = 0 # Rear

	def capacity(self):
		return self.cap # Return capacity

	def push_front(self, data):
		if self.size >= self.cap: # If size is greater than or equal to capacity
			self._resize() # Resize
		self.front = (self.front - 1 + self.cap) % self.cap # Front is front minus 1 plus capacity mod capacity
		self.data[self.front] = data # Data front is data
		self.size += 1 # Size is size plus 1

	def push_back(self, data):
		if self.size >= self.cap: # If size is greater than or equal to capacity
			self._resize() # Resize
		self.data[self.rear] = data # Data rear is data
		self.rear = (self.rear + 1) % self.cap # Rear is rear plus 1 mod capacity
		self.size += 1 # Size is size plus 1

	def pop_front(self):
		if self.is_empty(): # If is empty
			raise IndexError("pop_front() used on empty deque") # Raise index error
		front_data = self.data[self.front] # Front data is data front
		self.data[self.front] = None # Data front is none
		self.front = (self.front + 1) % self.cap # Front is front plus 1 mod capacity
		self.size -= 1 # Size is size minus 1
		return front_data # Return front data

	def pop_back(self):
		if self.is_empty(): # If is empty
			raise IndexError("pop_back() used on empty deque") # Raise index error
		self.rear = (self.rear - 1 + self.cap) % self.cap # Rear is rear minus 1 plus capacity mod capacity
		back_data = self.data[self.rear] # Back data is data rear
		self.data[self.rear] = None # Data rear is none
		self.size -= 1 # Size is size minus 1
		return back_data # Return back data

	def get_front(self):
		if self.is_empty(): # If is empty
			return None # Return none
		return self.data[self.front] # Return data front

	def get_back(self):
		if self.is_empty(): # If is empty
			return None # Return none
		return self.data[(self.rear - 1 + self.cap) % self.cap] # Return data rear minus 1 plus capacity mod capacity

	def is_empty(self):
		return self.size == 0 # Return size is equal to 0

	def __len__(self):
		return self.size # Return size

	def __getitem__(self, k):
		if k < 0 or k >= self.size: # If k is less than 0 or k is greater than or equal to size
			raise IndexError("Index out of range") # Raise index error
		return self.data[(self.front + k) % self.cap] # Return data front plus k mod capacity
	
	def _resize(self): # This function is used to resize the deque
		new_cap = self.cap * 2 # New capacity is capacity times 2
		new_data = [None] * new_cap # New data is none times new capacity
		for i in range(self.size): # For i in range size
			new_data[i] = self.data[(self.front + i) % self.cap] # New data i is data front plus i mod capacity
		self.data = new_data # Data is new data
		self.front = 0 # Front is 0
		self.rear = self.size # Rear is size
		self.cap = new_cap # Capacity is new capacity
