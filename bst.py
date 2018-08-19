from collections import deque


class bst :
	class node:
		def __init__(self,v):
			self.value=v
			self.left=None
			self.right=None
		def __gt__(self,other):
			return self.value > other 
		def __lt__(self,other):
			return self.value < other	

	def __init__(self):
		self.root=None

	def __insert(self,root,v):
		#  left for small
		if root is None:
			return self.node(v)
		if root < v :
			root.right=self.__insert(root.right,v)
		else :
			root.left=self.__insert(root.left,v)
		return root		

	def insert(self,v):
		self.root=self.__insert(self.root,v)	
	def __show(self,root):
		if root is None:
			return 

		print(root.value)
		self.__show(root.left)
		self.__show(root.right)
	def show(self):
		self.__show(self.root)
	def __height(self,root):
		if root is None:
			return 0
		u=self.__height(root.left)
		v=self.__height(root.right)
		return u+1 if u>v else v+1
	def height(self):
		return self.__height(self.root)	
	def __printlvl(self,root,lvl):
		if lvl is 1 :
			if root is None:
				return
			print(root.value)
			return 
		if root is not None :
			self.__printlvl(root.left,lvl-1)
			self.__printlvl(root.right,lvl-1)
		return	
	def printlvl(self,lvl):
		print("in level %s"%lvl)
		self.__printlvl(self.root,lvl)				
	def __lvl_order_rec(self,root,lvl):
		if root is None or lvl > self.height() :
			return
	
		self.printlvl(lvl)
		self.__lvl_order_rec(root,lvl+1)
	def lvl_order_rec(self):
		self.__lvl_order_rec(self.root,1)						

	def __inorder(self,root):
		if root is None:
			return 
		self.__inorder(root.left)	
		print(root.value)
		self.__inorder(root.right)
	def inorder(self):
		self.__inorder(self.root)	

	def __rev_inorder(self,root):
		if root is None:
			return 
		self.__rev_inorder(root.right)
		print(root.value)
		self.__rev_inorder(root.left)
	def rev_inorder(self):
		self.__rev_inorder(self.root)		

	def inorder_i(self):
		# need to be fixed
		# dosn't work
		d=deque()
		p=self.root
		def add_left(node):
			while node.left:
				node=node.left
				d.append(node)
		def add_right(node):
			while node and  node.right:
				node=node.right 
				d.append(node)		
		d.append(p)
		while d:
			add_left(p)
			p=d.pop()
			print(p.value)
			
	def __sum_tree(self,root):
		if root is None:
			return 0
		summ=self.__sum_tree(root.right)
		#print(summ)
		root.value+=summ
		#print(root.value)
		summ+=root.value
		#print(summ)
		summ+=self.__sum_tree(root.left)
		return summ
	def sum_tree(self):
		self.__sum_tree(self.root)	

	def lvl_order(self):
		d=deque()
		d.append(self.root)
		while d :
			tmp=d.popleft()
			if tmp.left:
				d.append(tmp.left)
			if tmp.right:
				d.append(tmp.right)
			print(tmp.value)			




'''
b=bst()
from random import randint
for i in range(10):
	b.insert(randint(-5,39))

#b.show()
b.insert(-7)
#print(b.height())

#b.printlvl(5)	

#b.lvl_order_rec()
b.inorder()
print("**********")
b.inorder_i()
'''