

from heap import heap 

class pq(heap):
	class element:
		def __init__(self,value,p=0):
			self.value=value
			self.p=p
		def __gt__(self,other):
			return self.p > other.p 			

	def __init__(self):
		super().__init__()
	# no point of this thou

	# insert will be the same 
	def pop(self):
		if not self:
			return
		tmp=self.list[1] # highest p 
		self.del_max()
		return tmp.value
		# i only do care about its value 
	
	def __next__(self):
		self.i+=1
		if self.i>self.size:
			raise StopIteration	
		return self.list[self.i].value

	def __iter__(self):
		self.i=0
		return self		



# tests 


h=pq()		
h.insert(h.element(1))
h.insert(h.element(1,2))
h.insert(h.element(3,5))
h.insert(h.element(3,2))

for i in h :
	print(i)
