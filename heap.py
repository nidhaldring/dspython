

class heap:
	# so this is a max heap
	# heap works as follow
	# if p is a parent than its greater than all its children
	def __init__(self):
		self.list=[0]
		#so that divison will be smoother
		self.size=0

	def precup(self):
		# so this methods fix the tree
		# if an element is inserted at a wrong position
		i=self.size
		while i//2>0:
			if self.list[i] > self.list[i//2]:
				self.list[i],self.list[i//2]=self.list[i//2],self.list[i]
				# smooth swap :v 
			i//=2
				

	def insert(self,value):
		self.list.append(value)
		self.size+=1
		if self.size is 1:
			return
		if self.list[self.size] > self.list[self.size//2]:
			self.precup()


	def show(self):
		for i in self.list:
			print(i)
	def show_in_lvl(self):
		c=1
		i=1
		while i <= self.size:
			print(self.list[i],end=' - ')
			i+=1
			if i==2**c:
				# since i implement heap using a complete binary tree
				c=i 
				print()


	def __bool__(self):
		return self.size is not  0	

	def del_max(self):
	#for tomorrow morning :)
	#morning aka 5 pm
	#non recursive way
	#+ my own idea
		i=1
		while 2*i+1 <= self.size:
			if self.list[2*i] > self.list[2*i+1]:
				self.list[i]=self.list[2*i]
				i*=2
			else:
				self.list[i]=self.list[2*i+1]
				i=2*i+1
		while i<self.size:
			self.list[i]=self.list[i+1]	
			i+=1
		self.list.pop()	
		self.size-=1 # very imporatant step i forgot :v

	def heapify(self,i):
	# recursive fucntion to keep the tree as a heap tree
	# basically swap till right postion is reached 
		if i == self.size:
			return
		m=i 
		if self.list[m] <self.list[2*i]:m=2*i
		if self.list[m]<self.list[2*i+1]:m=2*i+1
		if m != i :
		# if it's not the right postion for the parent than swap with m 
			self.list[i],self.list[m]=self.list[m],self.list[i]
			# smooth move 
			self.heapify(m)
		return 
	# the parent is in its right postion	

	def del_max_rec(self):
		self.list[1]=self.list[self.size]
		self.heapify(1)
		self.size-=1


	# my seventh sorting algoirthms	
	def heapsort(self,array):
		self.__init__()
		print(self.size)
		for i in array :
			self.insert(i)
		# make a heap from the array 
		i=0
		while i < len(array):
			array[i]=self.list[1]
			i+=1
			self.del_max()

	def __iter__(self):
		self.i=0
		return self
	def __next__(self):
		self.i+=1
		if self.i>self.size:
			raise StopIteration	
		return self.list[self.i]	






'''
h=heap()

h.insert(7)
h.insert(8)
h.insert(3)
h.insert(12)
h.insert(33)
h.insert(5)
h.insert(100)

h.show()
h.del_max()
print("*******")
h.show()
h.insert(100)
h.del_max_rec()
print('********')
h.show()
#h.show_in_lvl()
# works fine !! 
# annd does wut its supposed to do 
array=[1,5,9,8,6,3,2,0]

h.heapsort(array)

print(array)

'''