# Binary Search Recursive in python
 
def binarySearchR (array, x, low, high):
	"""
	Binary Search Algorithm
	Recursive Method

	binarySearch(arr, x, low, high)
    if low > high
        return False 
    else
        mid = (low + high) / 2 
        if x == arr[mid]
            return mid
        else if x < data[mid]        // x is on the right side
            return binarySearch(arr, x, mid + 1, high)
        else                               // x is on the right side
            return binarySearch(arr, x, low, mid - 1)

	Time Complexities

    Best case complexity: O(1)
    Average case complexity: O(log n)
    Worst case complexity: O(log n)


    Space Complexity: O(n)
	""" 

	if high >= low: 

		mid = low + (high - low)//2

		if array[mid] == x: 
			return mid 
		
		elif array[mid] > x: 
			return binarySearchR(array, x, low, mid-1) 
 
		else: 
			return binarySearchR(array, x, mid + 1, high) 

	else: 
		return -1

array = [ 3, 4, 5, 6, 7, 8, 9 ] 
x = 4

result = binarySearchR(array, x, 0, len(array)-1) 

if result != -1: 
	print("Element is present at index " + str(result))
else: 
	print ("Not found")