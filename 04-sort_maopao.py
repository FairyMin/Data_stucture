#coding:utf-8
def bubble_sort(alist):
	
	n = len(alist)
	for j in range(n-1):
		for i in range(0,n-j-1):
			if alist[i] > alist[i+1]:
				alist[i],alist[i+1] = alist[i+1],alist[i]
if __name__ == "__main__":
	li = [9,4,15,24,39,88,65,76]
	print(li)
	bubble_sort(li)
	print(li)



