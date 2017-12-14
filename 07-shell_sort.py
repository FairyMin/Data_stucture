def shell_sort(alist):
	'''shell sort '''
	n = len(alist)

	gap = n // 2
	#
	while gap > 0:

		for j in range(gap,n):
			i = j
			while i>0:
				if alist[i] < alist[i-gap]:
					alist[i],alist[i-gap] = alist[i-gap],alist[i]
					i -= gap
				else:
					break
		gap //= 2

if __name__ == "__main__":
	li  = [6,9,64,48,24,32,2,1]
	print(li)
	shell_sort(li)
	print(li)

