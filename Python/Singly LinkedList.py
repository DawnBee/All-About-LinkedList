class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def add_node(self, data):
		new_node = Node(data)

		if not self.head:
			self.head = new_node
			return
		current = self.head 

		while current.next:
			current = current.next
		current.next = new_node

	def show_nodes(self, head=None):
		if not head:
			current = self.head
		else:
			current = head

		while current:
			if current.next is None:
				print(current.data)
			else:
				print(current.data, end=" --> ")
			current = current.next

	def remove_duplicates(self):
		current = self.head 

		while current and current.next:
			if current.data == current.next.data:
				current.next = current.next.next
			else:
				current = current.next
		self.show_nodes()

	def remove_elements(self, val):
		dummy = Node(0)
		dummy.next = self.head
		current = dummy

		while current.next:
			if current.next.data == val:
				current.next = current.next.next
			else:
				current = current.next
		self.show_nodes()

	def merge_two_llist(self, llist_1, llist_2):
		merge_list = LinkedList()
		dummy = Node(0)
		tail = dummy 

		while llist_1 and llist_2:
			if llist_1.data < llist_2.data:
				tail.next = llist_1
				llist_1 = llist_1.next 
			else:
				tail.next = llist_2
				llist_2 = llist_2.next 
			tail = tail.next

		if llist_1:
			tail.next = llist_1
		elif llist_2:
			tail.next = llist_2

		tail = dummy.next
		self.show_nodes(tail)

	def get_intersection_node(self, head_A, head_B):
		pointer_a, pointer_b = head_A, head_B

		while pointer_a != pointer_b:
			pointer_a = pointer_a.next if pointer_a else head_B
			pointer_b = pointer_b.next if pointer_b else head_A

		if pointer_a:
			print(f"Intersected at: {pointer_a.data}")
		else:
			print("No Intersection!")

	#  Recursive
	def rec_reverse_list(self, head=None):
		if not head:
			head = self.head

		if head is None or head.next is None:
			return head

		new_head = self.rec_reverse_list(head.next)

		head.next.next = head
		head.next = None

		return new_head

	# Iterative
	def reverse_list(self):
		previous, current = None, self.head 

		while current:
			temp = current.next 
			current.next = previous
			previous = current
			current = temp

		self.show_nodes(previous)

	def get_decimal(self):
		current = self.head
		bin_strs = ""

		while current:
			bin_strs += str(current.data)
			current = current.next

		return int(bin_strs, 2)


	@property
	def list_length(self):
		current = self.head
		length = 0

		while current:
			length += 1
			current = current.next

		return length

	def middle_node(self):
		current = self.head 

		for i in range(self.list_length // 2):
			current = current.next

		self.show_nodes(current)	


	def remove_nth_from_end(self, n):
		if n <= 0:
			return

		dummy = Node(0)
		dummy.next = self.head 
		fast = dummy 
		slow = dummy 

		for _ in range(n):
			if not fast:
				return
			fast = fast.next 

		while fast.next:
			fast = fast.next 
			slow = slow.next 

		slow.next = slow.next.next 

		self.show_nodes(dummy.next)

	def has_cycle(self):
		# Floyd's Tortoise and Hare Algorithm
		slow, fast = self.head, self.head 

		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next 

			if slow == fast:
				return True
		return False

	def swapPairs(self):
		def swap(node_1, node_2):
			node_1.next = node_2.next
			node_2.next = node_1
			return node_2

		dummy = Node(0)
		dummy.next = self.head
		current = dummy

		while current.next and current.next.next:
			current.next = swap(current.next, current.next.next)
			current = current.next.next

		self.show_nodes(dummy.next)


llist = LinkedList() # Main class object

llist_1 = LinkedList()
llist_1.add_node(1)
llist_1.add_node(2)
llist_1.add_node(4)

llist_2 = LinkedList()
llist_2.add_node(1)
llist_2.add_node(3)
llist_2.add_node(4)

# Prints the nodes of both lists
# llist_1.show_nodes()
# llist_2.show_nodes()

# Merged Two LinkedList
# merged_list = llist_1.merge_two_llist(llist_1.head, llist_2.head)


# Head A
headA = LinkedList()
a1 = Node("a1")
a2 = Node("a2")
c1 = Node("c1")
c2 = Node("c2")
c3 = Node("c3")

a1.next = a2
a2.next = c1
c1.next = c2
c2.next = c3
headA.head = a1

# Head B
headB = LinkedList()
b1 = Node("b1")
b2 = Node("b2")
b3 = Node("b3")

b1.next = b2
b2.next = b3
b3.next = c1
headB.head = b1

# Returns the intersected node if it has
# intersected_node = llist.get_intersection_node(headA.head, headB.head)

nth_llist = LinkedList()
nth_llist.add_node(1)
nth_llist.add_node(2)
nth_llist.add_node(3)
nth_llist.add_node(4)
nth_llist.add_node(5)

# nth_llist.remove_nth_from_end(2)

# Reverse the List
# nth_llist.reverse_list()

dupl_llist = LinkedList()
dupl_llist.add_node(1)
dupl_llist.add_node(1)
dupl_llist.add_node(2)
dupl_llist.add_node(3)
dupl_llist.add_node(3)

# Starts at middle node
# dupl_llist.middle_node()

# Remove Duplicate Nodes
# dupl_llist.remove_duplicates()

# Remove an element
# dupl_llist.remove_elements(2)


# A cycled LinkedList
# Cycles will result to infinite loop when displayed
cyc_llist = LinkedList()
node_a = Node(3)
node_b = Node(2)
node_c = Node(0)
node_d = Node(-4)

node_a.next = node_b
node_b.next = node_c
node_c.next = node_d
node_d.next = node_b
cyc_llist.head = node_a

# print(cyc_llist.has_cycle())


# Binary LinkedList
deci_llist = LinkedList()
deci_llist.add_node(1)
deci_llist.add_node(0)
deci_llist.add_node(1)
# print(deci_llist.get_decimal())


swap_me = LinkedList()
swap_me.add_node(2)
swap_me.add_node(4)
swap_me.add_node(6)
swap_me.add_node(8)
swap_me.add_node(10)
swap_me.add_node(12)

# print("Before Swap:")
# swap_me.show_nodes()
# print("After Swap:")
# swap_me.swapPairs()