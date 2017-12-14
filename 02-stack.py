#coding:utf-8

class Stack(object):
	def __init__(self):
		self.__list =[]

	def push(self,item):
		'''add an element to the top of stack'''
		self.__list.append(item)
	
	def pop(self):
		'''pop an element of the stack'''
		return self.__list.pop()
		
	
	def peek(self):
		'''return the value of the element in the top '''
		if self.__list:
			return self.__list[-1]
		else:
			return NOne

	def is_empty(self):
		'''judge whether the stack is empty'''
		return self.__list == []

	def size(self):
		'''retuen the number of element'''
		return len(self.__list)

if __name__=="__main__":
		s = Stack()
		s.push(1)
		s.push(2)
		s.push(3)
		s.push(4)
		print(s.pop())
		print(s.pop())	
		print(s.pop())
		print(s.pop())
		
	
		s.push(2)
		s.push(2)
		s.push(2)
		s.push(2)
