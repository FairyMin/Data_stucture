
def select_sort(alist):
	"""xuan ze pai xu"""
	n = len(alist)
	for j in range(n-1):
		min_index = j
		for i in range(j+1,n):
			if alist[min_index] > alist[i]:
				min_index = i
		alist[j],alist[min_index] = alist[min_index],alist[j]

if __name__ == "__main__":
	li = [22,99,6,7,54,36]
	print(li)
	select_sort(li)
	print(li)


