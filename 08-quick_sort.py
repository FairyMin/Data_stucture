def quick_sort(alist,first,last):
	"""quick sort"""
	#n = len(alist)
	mid_value = alist[first]
	low = first
	high = last
	if first >= last:
		return

	while low < high:
		# high move left

		while low < high and alist[high] >= mid_value:
			high -= 1
		alist[low] = alist[high]
	
		
		#low move right
		while low < high and alist[low] < mid_value:
			low += 1
		alist[high] = alist[low]
	
	alist[low] = mid_value
	
	#sort left part 
	quick_sort(alist,first,low-1)
	
	#sort right part
	quick_sort(alist,low+1,last,)

if __name__ == "__main__":
	li = [45,33,65,88,76,3,9]
	print(li)
	quick_sort(li,0,len(li)-1)
	print(li)
