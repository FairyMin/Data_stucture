#coding:utf-8

class Queue(object):
	'''queue'''
	def __init__(self):
		self.__list = []

	def enqueue(self,item):
		'''add an element'''
		self.__list.append(item)

	def dequeue(self):
		'''delete na element '''
		return self.__list.pop(0)

	def is_empty(self):
		'''judge'''
		return self.__list == []

	def size(self):
		'''renturn the size  '''
		return len(self.__list)

if __name__ == "__main__":
	s = Queue()
	s.enqueue(1)
	s.enqueue(2)
	s.enqueue(3)
	s.enqueue(4)
	print(s.dequeue())
	print(s.dequeue())
	print(s.dequeue())
	print(s.dequeue())
