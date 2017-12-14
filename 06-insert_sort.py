#coding:utf-8
def insert_sort(alist):
	''' insert'''
	n =len(alist)
	for j in range(1,n):
		i = j
		while i > 0:
			if alist[i] < alist[i-1]:
				alist[i],alist[i-1] = alist[i-1],alist[i]
				i -= 1
			else:
				break


if __name__ == "__main__":
	li = [9,7,66,23,52,88]
	print(li)
	insert_sort(li)
	print(li)


