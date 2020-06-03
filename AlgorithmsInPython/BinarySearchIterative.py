# Binary Search Iterative in python
 
def binarySearchI (array, x, low, high):
    """
    Binary Search Algorithm
    Iteration Method

    do until the pointers low and high meet each other.
    mid = (low + high)/2
    if (x == arr[mid])
        return mid
    else if (x > A[mid]) // x is on the right side
        low = mid + 1
    else                       // x is on the left side
        high = mid - 1
    

    Time Complexities

    Best case complexity: O(1)
    Average case complexity: O(log n)
    Worst case complexity: O(log n)


    Space Complexity: O(n)
    """ 

    while low <= high: 
  
        mid = low + (high - low)//2
          
        if array[mid] == x: 
            return mid 
  
        elif array[mid] < x: 
            low = mid + 1
  
        else: 
            high = mid - 1
      
    return -1

if __name__ == '__main__':

    array = [ 3, 4, 5, 6, 7, 8, 9 ] 
    x = 4

    result = binarySearchI(array, x, 0, len(array)-1) 

    if result != -1: 
        print("Element is present at index " + str(result))
    else: 
        print ("Not found")